CREATE TABLE [IF NOT EXISTS] congress (
    ID integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    house_rep boolean,
    dob text,
    email text,
);

CREATE TABLE [IF NOT EXISTS] funding (
    ID integer PRIMARY KEY,
    congress_ID integer,
    organization_ID integer,
    donation_amount real,
    year integer
);

CREATE TABLE [IF NOT EXISTS] votes (
    ID integer PRIMARY KEY,
    congress_ID integer,
    bill_ID integer,
    vote integer,
);

CREATE TABLE [IF NOT EXISTS] bills (
    ID integer PRIMARY KEY,
    name text,
    hyperlink text,
    year integer
);

CREATE TABLE [IF NOT EXISTS] organizations (
    ID integer PRIMARY KEY,
    name text
);