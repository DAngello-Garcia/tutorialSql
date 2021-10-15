#Constraints o restricciones

# NOT NULL - Ensures that a column cannot have a NULL value
# UNIQUE - Ensures that all values in a column are different
# PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
# FOREIGN KEY - Prevents actions that would destroy links between tables
# CHECK - Ensures that the values in a column satisfies a specific condition
# DEFAULT - Sets a default value for a column if no value is specified
# CREATE INDEX - Used to create and retrieve data from the database very quickly

# CREATE TABLE Persons (
#     ID int NOT NULL,
#     LastName varchar(255) NOT NULL,
#     FirstName varchar(255) NOT NULL,
#     Age int
# );
# ALTER TABLE Persons
# MODIFY Age int NOT NULL; 

# CREATE TABLE Persons (
#     ID int NOT NULL,
#     LastName varchar(255) NOT NULL,
#     FirstName varchar(255),
#     Age int,
#     PRIMARY KEY (ID)
# );

# CREATE TABLE Persons (
#     ID int NOT NULL,
#     LastName varchar(255) NOT NULL,
#     FirstName varchar(255),
#     Age int,
#     UNIQUE (ID)
# ); 

# CREATE TABLE Orders (
#     OrderID int NOT NULL,
#     OrderNumber int NOT NULL,
#     PersonID int,
#     PRIMARY KEY (OrderID),
#     FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
# ); 

# CREATE TABLE Persons (
#     ID int NOT NULL,
#     LastName varchar(255) NOT NULL,
#     FirstName varchar(255),
#     Age int,
#     City varchar(255) DEFAULT 'Sandnes'
# ); 


#VARCHAR(SIZE)
# INT(SIZE)
# BIGINT(SIZE)
# FLOAT(SIZE)
# DECIMAL(SIZE)

# DATE     	A date. Format: YYYY-MM-DD. The supported range is from '1000-01-01' to '9999-12-31'
# DATETIME(FSP)  A date and time combination. Format: YYYY-MM-DD hh:mm:ss. The supported range is from '1000-01-01 00:00:00' to '9999-12-31 23:59:59'
#             Adding DEFAULT and ON UPDATE in the column definition to get automatic initialization and updating to the current date and time
#             An optional fsp value in the range from 0 to 6 may be given to specify fractional seconds precision
