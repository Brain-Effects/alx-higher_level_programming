#!/usr/bin/python3
/*
This script creates the table force_name with the columns id and name.
The id column is of type INT and the name column is of type VARCHAR(256) and can't be null.
If the table already exists, the script will not fail.
*/

-- Create table if not exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
