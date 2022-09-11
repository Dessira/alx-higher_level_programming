-- Creates the database hbtn_0d_usa and the table states
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.states (
	id int UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
