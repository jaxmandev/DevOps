SQL | Advanced Functions
Following are some of the advanced functions defined in SQL:

BIN(): It converts a decimal number to a binary number.
Syntax: SELECT BIN(18); Output:  

BINARY(): It converts a value to a binary string
Syntax: SELECT BINARY "GeeksforGeeks"; Output: 

COALESCE(): It returns the first non-null expression in a list.
Syntax: SELECT COALESCE(NULL,NULL,'GeeksforGeeks',NULL,'Geeks'); Output: 
CONNECTION_ID(): It returns the unique connection ID for the current connection.
Syntax:
SELECT CONNECTION_ID(); Output: 

CURRENT_USER(): It returns the user name and host name for the MySQL account used by the server to authenticate the current client.
Syntax: SELECT CURRENT_USER();
Output: 

DATABASE(): It returns the name of the default database.
Syntax: SELECT DATABASE(); Output: 

IF(): It returns one value if a condition is TRUE, or another value if a condition is FALSE.
Syntax: SELECT IF(200<500, "YES", "NO"); Output: 

LAST_INSERT_ID(): It returns the first AUTO_INCREMENT value that was set by the most recent INSERT or UPDATE statement.
Syntax: SELECT LAST_INSERT_ID();
Output: 

NULLIF(): It returns the first expression if the two expressions are not equal. If the expressions are equal, NULLIF returns a null value of the type of the first expression.
Syntax: SELECT NULLIF(25.11, 25); Output: 


Syntax: SELECT NULLIF(115, 115);
 Output: 
SESSION_USER(): It returns the user name and host name for the current MySQL user.
Syntax: SELECT SESSION_USER(); Output: 

SYSTEM_USER(): It returns the user name and host name for the current MySQL user.
Syntax: SELECT SYSTEM_USER(); Output: 

USER(): It returns the user name and host name for the current MySQL user.
Syntax: SELECT USER(); Output: 

VERSION(): It returns the version of the MySQL database.
Syntax: SELECT VERSION(); Output: 
