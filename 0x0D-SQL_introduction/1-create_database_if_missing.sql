-- Create the database 'hbtn_0c_0' if it doesn't already exist
-- This SQL script ensures that the database is created only if it's not present.

-- Check if the database 'hbtn_0c_0' already exists
-- If it doesn't exist, the following command will create it
CREATE DATABASE IF NOT EXISTS `hbtn_0c_0`;

-- The 'IF NOT EXISTS' clause prevents errors if the database already exists.
-- This allows the script to execute successfully even if the database is already created.
-- The backticks (`) around the database name are used for proper identifier quoting.
-- They're optional if the database name doesn't contain special characters.
