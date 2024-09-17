CREATE DATABASE maabara_mkononi;

CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON maabara_mkononi.* TO 'user'@'localhost';
FLUSH PIVILEGES;
