SQL | String functions are used to perform an operation on input string and return an output string.
Following are the string functions defined in SQL:

ASCII(): This function is used to find the ASCII value of a character.
Syntax: SELECT ascii('t');
Output: 116

CHAR_LENGTH(): Doesn’t work for SQL Server. Use LEN() for SQL Server. This function is used to find the length of a word.
Syntax: SELECT char_length('Hello!');
Output: 6

CHARACTER_LENGTH(): Doesn’t work for SQL Server. Use LEN() for SQL Server. This function is used to find the length of a line.
Syntax: SELECT CHARACTER_LENGTH('geeks for geeks');
Output: 15

CHARINDEX(): The CHARINDEX() function searches for a substring in a string, and returns the position as an INT. If the substring is not found, this function returns 0. Note: This function performs a case-insensitive search.
SELECT CHARINDEX('t', 'Customer') AS MatchPosition;

CONCAT(): This function is used to add two words or strings.
Syntax: SELECT column1 + ‘ ‘ + column2
FROM dual;
Output: Napoleon Bonaparte

CONCAT_WS(): This function is used to add two words or strings with a symbol as concatenating symbol.
Syntax: SELECT CONCAT_WS('_', 'geeks', 'for', 'geeks');
Output: geeks_for_geeks

FIND_IN_SET(): This function is used to find a symbol from a set of symbols.
Syntax: SELECT FIND_IN_SET('b', 'a, b, c, d, e, f');
Output: 2

FORMAT(): This function is used to display a number in the given format.
Syntax: Format("0.981", "Percent");
Output: ‘98.10%’

INSERT(): This function is used to insert the data into a database.
Syntax: INSERT INTO database (geek_id, geek_name) VALUES (5000, 'abc');
Output: successfully updated

INSTR(): This function is used to find the occurrence of an alphabet.
Syntax: INSTR('geeks for geeks', 'e');
Output: 2 (the first occurrence of ‘e’) Syntax: INSTR('geeks for geeks', 'e', 1, 2 );
Output: 3 (the second occurrence of ‘e’)

LCASE(): This function is used to convert the given string into lower case.
Syntax: LCASE ("GeeksFor Geeks To Learn");
Output: geeksforgeeks to learn

LEFT(): This function is used to SELECT a sub string from the left of given size or characters. Syntax: SELECT LEFT('geeksforgeeks.org', 5);
Output: geeks

LENGTH(): This function is used to find the length of a word.
Syntax: LENGTH('GeeksForGeeks');
Output: 13

LOCATE(): This function is used to find the nth position of the given word in a string.
Syntax: SELECT LOCATE('for', 'geeksforgeeks', 1);
Output: 6

LOWER(): This function is used to convert the upper case string into lower case.
Syntax: SELECT LOWER('GEEKSFORGEEKS.ORG');
Output: geeksforgeeks.org

LPAD(): This function is used to make the given string of the given size by adding the given symbol.
Syntax: LPAD('geeks', 8, '0');
Output:
000geeks

LTRIM(): This function is used to cut the given sub string from the original string.
Syntax: LTRIM('123123geeks', '123');
Output: geeks

MID(): This function is to find a word from the given position and of the given size.
Syntax: Mid ("geeksforgeeks", 6, 2);
Output: for

POSITION(): This function is used to find position of the first occurrence of the given alphabet. Syntax: SELECT POSITION('e' IN 'geeksforgeeks');
Output: 2

REPEAT(): This function is used to write the given string again and again till the number of times mentioned.
Syntax: SELECT REPEAT('geeks', 2);
Output: geeksgeeks

REPLACE(): This function is used to cut the given string by removing the given sub string.
Syntax: REPLACE('123geeks123', '123');
Output: geeks

REVERSE(): This function is used to reverse a string.
Syntax: SELECT REVERSE('geeksforgeeks.org');
Output: ‘gro.skeegrofskeeg’

RIGHT(): This function is used to SELECT a sub string from the right end of the given size. Syntax: SELECT RIGHT('geeksforgeeks.org', 4);
Output: ‘.org’

RPAD(): This function is used to make the given string as long as the given size by adding the given symbol on the right.
Syntax: RPAD('geeks', 8, '0');
Output: ‘geeks000’

RTRIM(): This function is used to cut the given sub string from the original string.
Syntax: RTRIM('geeksxyxzyyy', 'xyz');
Output: ‘geeks’

SPACE(): This function is used to write the given number of spaces.
Syntax: SELECT SPACE(7);
Output: ‘       ‘

STRCMP(): This function is used to compare 2 strings.
If string1 and string2 are the same, the STRCMP function will return 0.
If string1 is smaller than string2, the STRCMP function will return -1.
If string1 is larger than string2, the STRCMP function will return 1.
Syntax: SELECT STRCMP('google.com', 'geeksforgeeks.com');
Output: -1

SUBSTR(): This function is used to find a sub string from the a string from the given position. Syntax:SUBSTR('geeksforgeeks', 1, 5);
Output: ‘geeks’

SUBSTRING(): This function is used to find an alphabet from the mentioned size and the given string.
Syntax: SELECT SUBSTRING('GeeksForGeeks.org', 9, 1);
Output: ‘G’

SUBSTRING_INDEX(): This function is used to find a sub string before the given symbol.
Syntax: SELECT SUBSTRING_INDEX('www.geeksforgeeks.org', '.', 1);
Output: ‘www’

TRIM(): This function is used to cut the given symbol from the string.
Syntax: TRIM(LEADING '0' FROM '000123');
Output: 123

UCASE(): This function is used to make the string in upper case.
Syntax: UCASE ("GeeksForGeeks");
Output:
GEEKSFORGEEKS
