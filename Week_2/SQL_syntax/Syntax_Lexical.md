## SELECT DISTINCT Syntax
```
SELECT DISTINCT column1, column2, ...
FROM table_name;
```
## AND Syntax
```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```
## OR Syntax
```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```
## NOT Syntax
```
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```
## ORDER BY Syntax
```
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, …
```
## INSERT INTO Syntax
```
It is possible to write the INSERT INTO statement in two ways.
The first way specifies both the column names and the values to be inserted:
```
```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. The INSERT INTO syntax would be as follows:
INSERT INTO table_name
VALUES (value1, value2, value3, …);
```
## IS NULL Syntax
```
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```
## IS NOT NULL Syntax
```
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```
## UPDATE Syntax
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
## DELETE Syntax
```
DELETE FROM table_name WHERE condition;
```
## SQL Server / MS Access Syntax:
```
SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;
```
## MySQL Syntax:
```
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;
```
## MIN() Syntax MAX() Syntax
```
SELECT MIN(Price) AS SmallestPrice
FROM Products;
SELECT MAX(Price) AS LargestPrice
FROM Products;
```
## COUNT() Syntax
```
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```
## AVG() Syntax
```
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```
## SUM() Syntax
```
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```
## IN Syntax
```
The IN operator is a shorthand for multiple OR conditions
SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');
```
## BETWEEN Syntax
```
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```
## SQL JOIN
```
### INNER JOIN Syntax
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;
```
### The LEFT JOIN 
- returns all records from the left table (Customers), even if there are no matches in the right table (Orders).
### The FULL OUTER JOIN 
- returns all matching records from both tables whether the other table matches or not. So, if there are rows in "Customers" that do not have matches in "Orders", or if there are rows in "Orders" that do not have matches in "Customers", those rows will be listed as well.

## UNION Syntax GROUP BY Syntax
```
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```
The following SQL statement lists the number of customers in each country, sorted high to low:
## GROUP BY Syntax
```
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;
```
The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.
## HAVING Syntax
```
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```
## EXISTS Syntax
```
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
SQL EXISTS Examples
The following SQL statement returns TRUE and lists the suppliers with a product price less than 20:
Example:
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20);
```
## ANY Syntax
```
SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY
(SELECT column_name FROM table_name WHERE condition);
```
## ALL Syntax
```
SELECT column_name(s)
FROM table_name
WHERE column_name operator ALL
(SELECT column_name FROM table_name WHERE condition);
```
## SELECT INTO Syntax
```
Copy all columns into a new table:
SELECT *
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;
Copy only some columns into a new table:
SELECT column1, column2, column3, ...
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;
```
```
Tip: SELECT INTO can also be used to create a new, empty table using the schema of another. Just add a WHERE clause that causes the query to return no data:
SELECT * INTO newtable
FROM oldtable
WHERE 1 = 0;
```
## INSERT INTO SELECT Syntax
```
The INSERT INTO SELECT statement copies data from one table and inserts it into another table.
INSERT INTO SELECT requires that data types in source and target tables match
The existing records in the target table are unaffected
Copy all columns from one table to another table:
```
```
INSERT INTO table2
SELECT * FROM table1
WHERE condition;
Copy only some columns from one table into another table:
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;
```
## The SQL CASE Statement
```
The CASE statement goes through conditions and returns a value when the first condition is met (like an IF-THEN-ELSE statement). So, once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the ELSE clause.
If there is no ELSE part and no conditions are true, it returns NULL.
```
## CASE Syntax
```
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
```

## A stored procedure
```
- a prepared SQL code that you can save, so the code can be reused over and over again.
So if you have an SQL query that you write over and over again, save it as a stored procedure, and then just call it to execute it.
You can also pass parameters to a stored procedure, so that the stored procedure can act based on the parameter value(s) that is passed.
Stored Procedure Syntax
CREATE PROCEDURE procedure_name
AS sql_statement
GO;
```
- Execute a Stored Procedure
EXEC procedure_name;


## DATABASE STATEMENTS

- CREATE DATABASE testDB;
The CREATE DATABASE statement is used to create a new SQL database.

- DROP DATABASE testDB;
statement drops the existing database “testDB":

- BACKUP DATABASE databasename
- TO DISK = ‘filepath’;
used in SQL Server to create a full back up of an existing SQL database.

- BACKUP DATABASE databasename
- TO DISK = 'filepath'
WITH DIFFERENTIAL;
- A differential back up only backs up the parts of the database that have changed since the last full database backup.

- The CREATE TABLE statement is used to create a new table in a database.
Syntax
```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```
### Create Table Using Another Table
```
CREATE TABLE new_table_name AS
    SELECT column1, column2,...
    FROM existing_table_name
    WHERE ….;
```
- DROP TABLE table_name;

### ALTER TABLE - ADD Column
To add a column in a table, use the following syntax:
```
ALTER TABLE Customers
ADD Email varchar(255);
```
### Delete a column in a table
(notice that some database systems don't allow deleting a column):
```
ALTER TABLE table_name
DROP COLUMN column_name;
```

### Change the data type of a column in a table, use the following syntax:
```
SQL Server / MS Access:
ALTER TABLE table_name
ALTER COLUMN column_name datatype;
```
- Constraints can be specified when the table is created with the CREATE TABLE statement, or after the table is created with the ALTER TABLE statement.
### Syntax
```
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
    ....
);
```
The following constraints are commonly used in SQL:
1. NOT NULL - Ensures that a column cannot have a NULL value
2. UNIQUE - Ensures that all values in a column are different
3. PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
4. FOREIGN KEY - Uniquely identifies a row/record in another table
5. CHECK - Ensures that all values in a column satisfies a specific condition
6. DEFAULT - Sets a default value for a column when no value is specified
7. INDEX - Used to create and retrieve data from the database very quickly

### A FOREIGN KEY 
- is a field (or collection of fields) in one table that refers to the PRIMARY KEY in another table.

### SQL CHECK on CREATE TABLE
- The following SQL creates a CHECK constraint on the "Age" column when the "Persons" table is created. The CHECK constraint ensures that the age of a person must be 18, or older:
```
MySQL:
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);
```
```
SQL Server / Oracle / MS Access:
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int CHECK (Age>=18)
);
```
