-- a script that creates the table force_name on your MySQL server
-- force_name desccription:
-- id INT
--name VARCHAR(256) can't be null

CREATE TABLE IF NOT EXISTS 'force_name'(
	id INT,
	name VARCHAR(2560) NOT NULL
);
