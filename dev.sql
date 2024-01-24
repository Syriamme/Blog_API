-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS my_database;
CREATE USER IF NOT EXISTS 'Daniel'@'localhost' IDENTIFIED BY 'new_password';
GRANT ALL PRIVILEGES ON `my_database`.* TO 'Daniel'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'Daniel'@'localhost';
FLUSH PRIVILEGES;
