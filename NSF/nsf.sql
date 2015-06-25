

%% PersonID	FirstName	LastName	Email	Institution

CREATE TABLE grantees(
id TEXT PRIMARY KEY,
first_name TEXT,
last_name TEXT,
email TEXT,
institution TEXT
)

%% Title	EffDate	ExpirDate	Amount	Directorate	Division	Abstract	AwardID

CREATE TABLE grants(
award_id TEXT PRIMARY KEY,
title TEXT,
effective_date date,
expiration_date date,
amount integer,
directorate TEXT,
division TEXT,
abstract TEXT
)

CREATE TABLE grants_for(
award_id TEXT REFERENCES grants(award_id), 
grantee_id TEXT REFERENCES grantees(id)
)

COPY grantees(id, first_name, last_name, email, institution)
FROM '/home/ubuntu/GovLab_OpenNYU/people.csv'
WITH DELIMITER ',' CSV HEADER

COPY grants(title, effective_date, expiration_date, amount, directorate, division, abstract, award_id)
FROM '/home/ubuntu/GovLab_OpenNYU/grants.csv'
WITH DELIMITER ',' CSV HEADER

COPY grants_for(grantee_id, award_id)
FROM '/home/ubuntu/GovLab_OpenNYU/grantfor.csv'
WITH DELIMITER ',' CSV HEADER

DELETE FROM grants_for;
DELETE FROM grants;
DELETE FROM grantees;



