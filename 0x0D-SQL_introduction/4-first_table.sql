-- This script creates the database hbtn_0c_0 if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Switch to the database hbtn_0c_0
USE hbtn_0c_0;

-- This script creates the table first_table in the current database if it doesn't already exist.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
