


drop table if exists project cascade;
CREATE TABLE project
(

    project_id INTEGER  PRIMARY KEY CHECK (project_id > 9999 AND project_id <=99999),
    project_name VARCHAR(100),
    project_start_date Date,
    project_completion_date Date,
    postcode INTEGER CHECK (postcode > 9999 AND postcode <=99999),
    bbl BIGINT
);



drop table if exists building_address;

CREATE TABLE building_address
(   
    building_id INTEGER PRIMARY KEY,
    borough VARCHAR(50) ,
    street_name VARCHAR(128),
    house_number VARCHAR(128),
    project_id INTEGER  CHECK (project_id > 9999 AND project_id <=99999),
    latitude DECIMAL,
    longitude DECIMAL,
    FOREIGN KEY  ( project_id ) REFERENCES project(project_id)

);



drop table if exists house_description;

CREATE TABLE house_description
(
    total_units INTEGER,
    counted_rental_units INTEGER,
    counted_home_ownership_units INTEGER,
    _1_br_units INTEGER,
    _2_br_units INTEGER,
    _3_br_units INTEGER,
    _4_br_units INTEGER,
    _5_br_units INTEGER,
    _6_br_units INTEGER,
    project_id INTEGER  CHECK (project_id > 9999 AND project_id <=99999),
    FOREIGN KEY  ( project_id ) REFERENCES project(project_id)

);


drop table if exists house_affordability;

CREATE TABLE house_affordability
(
    prevailing_wage_status VARCHAR(50),
    low_income_units INTEGER,
    middle_income_units INTEGER,
    moderate_income_units INTEGER,
    extremely_low_income_units INTEGER,
    very_low_income_units INTEGER,
    project_id INTEGER  CHECK (project_id > 9999 AND project_id <=99999),
    FOREIGN KEY  ( project_id ) REFERENCES project(project_id)

);



-- # Supporting Datasets

drop table if exists retail_store;

CREATE TABLE retail_store
(   
    store_name VARCHAR(128),
    street_address VARCHAR(128),
    borough VARCHAR(20),
    zip_code INTEGER CHECK (zip_code > 9999 AND zip_code <= 99999) ,
    bbl BIGINT,
    latitude DECIMAL,
    longitude DECIMAL

);



drop table if exists hospital;

CREATE TABLE hospital
(   
    facility_type VARCHAR(128),
    facility_name VARCHAR(128),
    postcode INTEGER CHECK (postcode > 9999 AND postcode <= 99999),
    borough VARCHAR(20)  ,
    location_1 VARCHAR(128),
    phone VARCHAR,
    latitude DECIMAL,
    longitude DECIMAL

);



drop table  if exists  user_login_details;
CREATE TABLE user_login_details
(
userid VARCHAR(16),
passw VARCHAR(100),
stamp timestamp NOT NULL

);


drop table  if exists  users;
CREATE TABLE users
(
userid VARCHAR(16),
passw VARCHAR(100),
mail VARCHAR(100)

);

drop table  if exists  user_logs;
CREATE TABLE user_logs
(
userid VARCHAR(16),
table_name VARCHAR(30),
stamp timestamp,
operation VARCHAR(50)
);



-- #################### USERS ###############################
-- Other users 
GRANT ALL PRIVILEGES ON DATABASE project TO admin;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin;


-- INSERT into users values ('student1','abc123','Viewer','student1@gmail.com',9748282182);


-- ####################   PRIVILEGES ############################




-- GRANT SELECT ON table project TO student1;
-- GRANT SELECT ON table retail_store TO student1;
-- GRANT SELECT ON table building_address TO student1;
-- GRANT SELECT ON table house_affordability TO student1;
-- GRANT SELECT ON table house_description TO student1;
-- GRANT SELECT ON table hospital TO student1;


-- GRANT UPDATE ON table project TO student1;
-- GRANT UPDATE ON table retail_store TO student1;
-- GRANT UPDATE ON table building_address TO student1;
-- GRANT UPDATE ON table house_affordability TO student1;
-- GRANT UPDATE ON table house_description TO student1;
-- GRANT UPDATE ON table hospital TO student1;


-- GRANT INSERT ON table project TO student1;
-- GRANT INSERT ON table retail_store TO student1;
-- GRANT INSERT ON table building_address TO student1;
-- GRANT INSERT ON table house_affordability TO student1;
-- GRANT INSERT ON table house_description TO student1;
-- GRANT INSERT ON table hospital TO student1;

-- GRANT DELETE ON table project TO student1;
-- GRANT DELETE ON table retail_store TO student1;
-- GRANT DELETE ON table building_address TO student1;
-- GRANT DELETE ON table house_affordability TO student1;
-- GRANT DELETE ON table house_description TO student1;
-- GRANT DELETE ON table hospital TO student1;






-- ##########################   AUDITS ######################################



drop table if exists project_audit;
create table project_audit

                  (

                  op  char(1)   NOT NULL,

                 stamp  timestamp NOT NULL,

                 user_id char(20)    NOT NULL,

    project_id INTEGER  PRIMARY KEY,
    project_name VARCHAR(100),
    project_start_date Date,
    project_completion_date Date,
    postcode INTEGER ,
    bbl BIGINT

                 );


create or replace function project_audit_information() returns trigger  

                 as  

                 $project_audit$

                 begin

                 if (TG_OP = 'DELETE') THEN

                 insert into project_audit SELECT 'D', now(), user, OLD.*;

                 elsif (TG_OP = 'UPDATE') THEN

                 insert into project_audit SELECT 'U', now(), user, NEW.*;

                 elsif (TG_OP = 'INSERT') THEN

                 insert into project_audit SELECT 'I', now(), user, NEW.*;

                 end if;

                 return null;

                 end;

                 $project_audit$ 

                 language plpgsql;

drop trigger if exists project_audit_trigger on project;
create trigger project_audit_trigger

                  after insert or update or delete on project

                  for each row 

                  execute procedure project_audit_information();




-- ########################################################
drop table if exists retail_store_audit;
create table retail_store_audit

                  (

                  op  char(1)   NOT NULL,

                 stamp  timestamp NOT NULL,

                 user_id char(20)    NOT NULL,

    store_name VARCHAR(128),
    street_address VARCHAR(128),
    borough VARCHAR(20),
    zip_code INTEGER CHECK (zip_code > 9999 AND zip_code <= 99999) ,
    bbl BIGINT,
    latitude DECIMAL,
    longitude DECIMAL

                 );


create or replace function retail_store_audit_information() returns trigger  

                 as  

                 $retail_store_audit$

                 begin

                 if (TG_OP = 'DELETE') THEN

                 insert into retail_store_audit SELECT 'D', now(), user, OLD.*;

                 elsif (TG_OP = 'UPDATE') THEN

                 insert into retail_store_audit SELECT 'U', now(), user, NEW.*;

                 elsif (TG_OP = 'SELECT') THEN

                 insert into retail_store_audit SELECT 'S', now(), user, NEW.*;

                 elsif (TG_OP = 'INSERT') THEN

                 insert into retail_store_audit SELECT 'I', now(), user, NEW.*;

                 end if;

                 return null;

                 end;

                 $retail_store_audit$ 

                 language plpgsql;


drop trigger if exists retail_store_audit_trigger on retail_store;
create trigger retail_store_audit_trigger

                  after insert or update or delete on retail_store

                  for each row 

                  execute procedure retail_store_audit_information();


-- ####################################################################


drop table if exists building_address_audit;
create table building_address_audit

                  (

                  op  char(1)   NOT NULL,

                 stamp  timestamp NOT NULL,

                 user_id char(20)    NOT NULL,

    building_id INTEGER PRIMARY KEY,
    borough VARCHAR(50) ,
    street_name VARCHAR(128),
    house_number VARCHAR(128),
    project_id INTEGER  CHECK (project_id > 9999 AND project_id <=99999),
    latitude DECIMAL,
    longitude DECIMAL

                 );


create or replace function building_address_audit_information() returns trigger  

                 as  

                 $building_address_audit$

                 begin

                 if (TG_OP = 'DELETE') THEN

                 insert into building_address_audit SELECT 'D', now(), user, OLD.*;

                 elsif (TG_OP = 'UPDATE') THEN

                 insert into building_address_audit SELECT 'U', now(), user, NEW.*;

                 elsif (TG_OP = 'INSERT') THEN

                 insert into building_address_audit SELECT 'I', now(), user, NEW.*;

                 end if;

                 return null;

                 end;

                 $building_address_audit$ 

                 language plpgsql;

drop trigger if exists building_address_audit_trigger on building_address;
create trigger building_address_audit_trigger

                  after insert or update or delete on building_address

                  for each row 

                  execute procedure building_address_audit_information();


-- ##############################################################################



drop table if exists house_description_audit;
create table house_description_audit

                  (

                  op  char(1)   NOT NULL,

                 stamp  timestamp NOT NULL,

                 user_id char(20)    NOT NULL,

    total_units INTEGER,
    counted_rental_units INTEGER,
    counted_home_ownership_units INTEGER,
    _1_br_units INTEGER,
    _2_br_units INTEGER,
    _3_br_units INTEGER,
    _4_br_units INTEGER,
    _5_br_units INTEGER,
    _6_br_units INTEGER,
    project_id INTEGER  CHECK (project_id > 9999 AND project_id <=99999)

                 );


create or replace function house_description_audit_information() returns trigger  

                 as  

                 $house_description_audit$

                 begin

                 if (TG_OP = 'DELETE') THEN

                 insert into house_description_audit SELECT 'D', now(), user, OLD.*;

                 elsif (TG_OP = 'UPDATE') THEN

                 insert into house_description_audit SELECT 'U', now(), user, NEW.*;

                 elsif (TG_OP = 'INSERT') THEN

                 insert into house_description_audit SELECT 'I', now(), user, NEW.*;

                 end if;

                 return null;

                 end;

                 $house_description_audit$ 

                 language plpgsql;

drop trigger if exists house_description_audit_trigger on house_description;
create trigger house_description_audit_trigger

                  after insert or update or delete on house_description

                  for each row 

                  execute procedure house_description_audit_information();

-- ######################################################################



drop table if exists house_affordability_audit;
create table house_affordability_audit

                  (

                  op  char(1)   NOT NULL,

                 stamp  timestamp NOT NULL,

                 user_id char(20)    NOT NULL,

    prevailing_wage_status VARCHAR(50),
    low_income_units INTEGER,
    middle_income_units INTEGER,
    moderate_income_units INTEGER,
    extremely_low_income_units INTEGER,
    very_low_income_units INTEGER,
    project_id INTEGER  CHECK (project_id > 9999 AND project_id <=99999)

                 );


create or replace function house_affordability_audit_information() returns trigger  

                 as  

                 $house_affordability_audit$

                 begin

                 if (TG_OP = 'DELETE') THEN

                 insert into house_affordability_audit SELECT 'D', now(), user, OLD.*;

                 elsif (TG_OP = 'UPDATE') THEN

                 insert into house_affordability_audit SELECT 'U', now(), user, NEW.*;

                 elsif (TG_OP = 'INSERT') THEN

                 insert into house_affordability_audit SELECT 'I', now(), user, NEW.*;

                 end if;

                 return null;

                 end;

                 $house_affordability_audit$ 

                 language plpgsql;

drop trigger if exists house_affordability_audit_trigger on house_affordability;
create trigger house_affordability_audit_trigger

                  after insert or update or delete on house_affordability

                  for each row 

                  execute procedure house_affordability_audit_information();


-- ############################################### Hospital Audit ##################################



drop table if exists hospital_audit;
create table hospital_audit

                  (

                  op  char(1)   NOT NULL,

                 stamp  timestamp NOT NULL,

                 user_id char(20)    NOT NULL,

    facility_type VARCHAR(128),
    facility_name VARCHAR(128),
    postcode INTEGER CHECK (postcode > 9999 AND postcode <= 99999),
    borough VARCHAR(20)  ,
    location_1 VARCHAR(128),
    phone VARCHAR,
    latitude DECIMAL,
    longitude DECIMAL

                 );


create or replace function hospital_audit_information() returns trigger  

                 as  

                 $hospital_audit$

                 begin

                 if (TG_OP = 'DELETE') THEN

                 insert into hospital_audit SELECT 'D', now(), user, OLD.*;

                 elsif (TG_OP = 'UPDATE') THEN

                 insert into hospital_audit SELECT 'U', now(), user, NEW.*;

                 elsif (TG_OP = 'INSERT') THEN

                 insert into hospital_audit SELECT 'I', now(), user, NEW.*;

                 end if;

                 return null;

                 end;

                 $hospital_audit$ 

                 language plpgsql;

drop trigger if exists hospital_audit_trigger on hospital;

create trigger hospital_audit_trigger

                  after insert or update or delete on hospital

                  for each row 

                  execute procedure hospital_audit_information();


