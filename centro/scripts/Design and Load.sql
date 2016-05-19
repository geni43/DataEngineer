
--object-relational database system : Postgres 

--Create Table sample_salesperson

CREATE TABLE sample_salesperson(
	salesperson_id int NOT NULL,
	salesperson_name varchar(50) NULL,
	title varchar(50) NULL,
	sales_manager_id int NULL,
	sales_manager_name varchar(50) NULL,
	sales_director_id int NULL,
	sales_director_name varchar(50) NULL,
	sales_vp_id int NULL,
	sales_vp_name varchar(50) NULL,
	sales_team_id int NULL,
	sales_team_name varchar(50) NULL)

--Load data to sample_salesperson

COPY sample_salesperson FROM 'C:\Users\nsrin\Documents\GitHub\DataEngineer\centro\data\sample_salesperson.csv' WITH DELIMITER ',' CSV HEADER;


--Add Primary key
ALTER TABLE sample_salesperson
  ADD CONSTRAINT salesperson_id_pk 
    PRIMARY KEY (salesperson_id);





CREATE TABLE sample_campaigns(
	campaign_id varchar(50) NULL,
	campaign_status varchar(50) NULL,
	campaign_ordered_at timestamp NULL,
	next_revision_ordered_at timestamp NULL,
	revision_number int NULL,
	is_last_ordered_campaign char(10) NULL,
	campaign_start_date date NULL,
	campaign_end_date date NULL,
	salesperson_id int NULL,
	gross_revenue float NULL,
	net_revenue float NULL
) 


-- Load data sample_campaigns
COPY sample_campaigns FROM 'C:\Users\nsrin\Documents\GitHub\DataEngineer\centro\data\sample_campaigns.csv' WITH DELIMITER ',' CSV HEADER;


--Add foreign key
ALTER TABLE sample_campaigns ADD  FOREIGN KEY(salesperson_id) REFERENCES sample_salesperson(salesperson_id);
