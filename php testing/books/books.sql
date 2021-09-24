CREATE DATABASE books;
USE books;
CREATE TABLE books (
	ID INT PRIMARY KEY,
	Title VARCHAR(100) NOT NULL,
	YearPublished INT NOT NULL,
	Edition INT NOT NULL,
	Publisher VARCHAR(60) NOT NULL,
	Authors VARCHAR(120) NOT NULL
);

INSERT INTO books VALUES
(1, "The C++ Programming Language", 2013, 4, "Addison-Wesley", "Bjarne Stroustrup"),
(2, "Java in a Nutshell", 2015, 6, "O'Reilly", "Benjamin J. Evans and David Flanagan"),
(3, "C# in Depth", 2018, 4, "Manning", "Jon Skeet"),
(4, "Designing Web APIs", 2018, 1, "O'Reilly", "Brenda Jin, Saurabh Sahni, and Amir Shevat");