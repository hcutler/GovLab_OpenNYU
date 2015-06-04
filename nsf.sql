

%% PersonID	FirstName	LastName	Email	Institution

CREATE TABLE grantees(
id TEXT PRIMARY KEY,
first_name TEXT,
last_name TEXT,
email TEXT,
institution TEXT
)

%% PersonID	Title	EffDate	ExpirDate	Amount	Directorate	Division	Abstract	AwardID

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

