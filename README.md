# SQL Queries
## There are many different types of SQL queries:

- CREATE: Used to create new database objects, such as tables, indexes, and views.
- INSERT: Used to insert new rows into a table.
- SELECT: Used to retrieve data from a database.
- UPDATE: Used to modify existing records in a table.
- DELETE: Used to delete records from a table.
- DROP: Used to delete database objects, such as tables, indexes, and views.
SQL queries are executed using the execute and executemany methods.

## Creating a Table
To create a table, use the following syntax:

```SQL
CREATE TABLE <table_name>
(column1 datatype,
 column2 datatype,
 ...);
```

## You can also create a table only if it doesn't exist:

```SQL
CREATE TABLE IF NOT EXISTS <table_name>
(column1 datatype,
 column2 datatype,
 ...);
```

## Common data types include:

- NULL: Represents a missing or unknown value.
- INTEGER: Stores integer numbers.
- REAL: Stores floating-point numbers.
- TEXT: Stores text strings.
- BLOB: Stores binary large objects, such as images or audio files.
You can also add constraints to columns, such as NOT NULL to ensure a value is always provided.

## Inserting Data
To insert a new row into a table, use the INSERT INTO statement:

```SQL
INSERT INTO <table_name> VALUES (value1, value2, ...);
```

## You can also specify the columns:

```SQL
INSERT INTO <table_name> (column1, column2) VALUES (value1, value2);
```

## Or use placeholders:

```SQL
cur.execute("INSERT INTO movie (title, year) VALUES (?, ?)", ('The Imitation Game', 2014))
```

## To insert multiple rows, use executemany:

```SQL
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    # ...
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
```

## Selecting Data
To retrieve data from a table, use the SELECT statement:

```SQL
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

## You can sort the results using ORDER BY:

```SQL
SELECT score, title
FROM movie
ORDER BY score;
```

## Updating Data
To modify existing records, use the UPDATE statement:

```SQL
UPDATE table_name
SET column1 = new_value, column2 = new_value, ...
WHERE condition;
```

## Deleting Data
To delete records, use the DELETE statement:

```SQL
DELETE FROM table_name
WHERE condition;
```

## Dropping a Table
To delete a table, use the DROP TABLE statement:

```SQL
DROP TABLE table_name;
```







