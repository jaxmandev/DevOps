--Increase income of all employees by 5% in a tbale
UPDATE employees
SET income = income * 1.05;

-- Find names of employees starting with 'A'
SELECT FirstNames, LastNames
FROM employees
WHERE FirstNames, LastNames
LIKE 'A%'

-- Find the number of employees working department 'ABC'
SELECT COUNT(*)
FROM employees
WHERE department_name = 'ABC';

-- Print details of employees whose first name ends with 'A'
-- and contains 6 charcaters
SELECT *
FROM employees
WHERE FirstNames LIKE '_____A';

-- Print details of employees who salary lies between 10 000 and 50 000
SELECT *
FROM employees
WHERE salary
BETWEEN 10000 AND 50000;

-- SELECT all records where the value of the City column starts with letter "a" and ends with the letter "b".
SELECT * FROM Customers
WHERE City LIKE 'a%b';

-- Select all records where the first letter of the City is an "a" or a "c" or an "s".
SELECT * FROM Customers
WHERE City LIKE '[acs]%';

-- Select all records where the first letter of the City starts with anything from an "a" to an "f".
SELECT * FROM Customers
WHERE City LIKE '[a-f]%';

-- Select all records where the first letter of the City is NOT an "a" or a "c" or an "f".
SELECT * FROM Customers
WHERE City LIKE '[^acf]%';

--List the number of customers in each country.
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;

-- List the number of customers in each country, ordered by the country with the most customers first.
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;

-- How many Employees have a home City of London?
SELECT COUNT(*) FROM Employees WHERE City = 'London';
-- Which Employee is a Doctor?
SELECT * FROM Employees WHERE TitleOfCourtesy = 'Dr.';
-- How many Products are discontinued?
SELECT COUNT(*) FROM Products WHERE Discontinued = 1;
-- What are the names and product IDs of the products with a unit price below 5.00?
SELECT ProductName, ProductID FROM Products WHERE UnitPrice < 5.00;
-- Which categories have a category name with initials beginning with B or S?
SELECT * FROM Categories WHERE CategoryName LIKE 'B%' OR CategoryName LIKE 'S%';
-- How many orders are there for EmployeeIDs 5 and 7 (The total for both)
SELECT COUNT(*) FROM Orders WHERE EmployeeID = 5 OR EmployeeID = 7;
-- Write a SELECT using the Employees table and concatenate First Name and Last Name together. Use a column alias to rename the column to Employee Name.
SELECT FirstName + ' ' + LastName
AS 'Employee Name'
FROM Employees;
-- Write a SELECT statement to list the six countries that have Region Codes in the Customers Table.
SELECT DISTINCT(Country) FROM Customers WHERE Region LIKE '%';
SELECT * FROM Customers;
