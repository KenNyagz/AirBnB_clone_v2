-- create database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user if doesn't exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- enabale privileges on the database to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant select privileges to the db schema to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
