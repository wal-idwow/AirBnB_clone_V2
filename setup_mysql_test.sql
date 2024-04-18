-- -- Creates the hbnb_test_db database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- -- Creates the hbnb_test user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- -- Grants all privileges on hbnb_test_db to hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';


-- Grants SELECT privilege on performance_schema to hbnb_test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
