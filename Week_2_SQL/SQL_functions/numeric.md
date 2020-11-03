SQL |  Numeric Functions are used to perform operations on numbers and return numbers.
Following are the numeric functions defined in SQL:

ABS(): It returns the absolute value of a number. Syntax: SELECT ABS(-243.5); Output: 243.5 SQL> SELECT ABS(-10);
+--------------------------------------+
| ABS(10)                                                  
+--------------------------------------+
| 10                                                       
+--------------------------------------+

ACOS(): It returns the cosine of a number. Syntax:  SELECT ACOS(0.25); Output: 1.318116071652818

ASIN(): It returns the arc sine of a number. Syntax: SELECT ASIN(0.25); Output: 0.25268025514207865

ATAN(): It returns the arc tangent of a number. Syntax: SELECT ATAN(2.5); Output: 1.1902899496825317

CEIL(): It returns the smallest integer value that is greater than or equal to a number. Syntax: SELECT CEIL(25.75); Output: 26

CEILING(): It returns the smallest integer value that is greater than or equal to a number. Syntax: SELECT CEILING(25.75); Output: 26

COS(): It returns the cosine of a number. Syntax: SELECT COS(30); Output: 0.15425144988758405

COT(): It returns the cotangent of a number. Syntax: SELECT COT(6); Output: -3.436353004180128

DEGREES(): It converts a radian value into degrees. Syntax: SELECT DEGREES(1.5); Output: 85.94366926962348 SQL>SELECT DEGREES(PI());
+------------------------------------------+
| DEGREES(PI())                                           
+------------------------------------------+
| 180.000000                                              
+------------------------------------------+
DIV(): It is used for integer division. Syntax: SELECT 10 DIV 5; Output: 2

EXP(): It returns e raised to the power of number. Syntax: SELECT EXP(1); Output: 2.718281828459045

FLOOR(): It returns the largest integer value that is less than or equal to a number. Syntax: SELECT FLOOR(25.75); Output: 25

GREATEST(): It returns the greatest value in a list of expressions. Syntax: SELECT GREATEST(30, 2, 36, 81, 125); Output: 125

LEAST(): It returns the smallest value in a list of expressions. Syntax: SELECT LEAST(30, 2, 36, 81, 125); Output: 2

LN(): It returns the natural logarithm of a number. Syntax: SELECT LN(2); Output: 0.6931471805599453

LOG10(): It returns the base-10 logarithm of a number. Syntax: SELECT LOG(2); Output: 0.6931471805599453

LOG2(): It returns the base-2 logarithm of a number. Syntax: SELECT LOG2(6); Output: 2.584962500721156

MOD(): It returns the remainder of n divided by m. Syntax: SELECT MOD(18, 4); Output: 2

PI(): It returns the value of PI displayed with 6 decimal places. Syntax: SELECT PI(); Output: 3.141593

POW(): It returns m raised to the nth power. Syntax: SELECT POW(4, 2); Output: 16

RADIANS(): It converts a value in degrees to radians. Syntax: SELECT RADIANS(180); Output: 3.141592653589793

RAND(): It returns a random number. Syntax: SELECT RAND(); Output: 0.33623238684258644

ROUND(): It returns a number rounded to a certain number of decimal places. Syntax: SELECT ROUND(5.553); Output: 6

SIGN(): It returns a value indicating the sign of a number. Syntax: SELECT SIGN(255.5); Output: 1

SIN(): It returns the sine of a number. Syntax: SELECT SIN(2); Output: 0.9092974268256817

SQRT(): It returns the square root of a number. Syntax: SELECT SQRT(25); Output: 5

TAN(): It returns the tangent of a number. Syntax: SELECT TAN(1.75); Output: -5.52037992250933

ATAN2(): It returns the arctangent of the x and y coordinates, as an angle and expressed in radians. Syntax: SELECT ATAN2(7); Output: 1.42889927219073

TRUNCATE(): This doesn’t work for SQL Server. It returns 7.53635 truncated to 2 places right of the decimal point. Syntax: SELECT TRUNCATE(7.53635, 2); Output: 7.53
