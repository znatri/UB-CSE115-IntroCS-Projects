import sqlite3

conn = sqlite3.connect('file.db') # Initiale sqlite3 and set up a connection

cur = conn.cursor() # Get Cursor for database

# Create/ Read/ Update/ Delete things in database. [CRUD - Acronym]

# Make a table with columns
# Command: CREATE TABLE IF NOT EXISTS table_name (table_columns)
cur.execute('CREATE TABLE IF NOT EXISTS ' + 'movies (title, year)')

# Insert a row into columns
# Command: INSERT INTO table_name VALUES (table_column_val)
cur.execute('INSERT INTO movies VALUES ("Jaws", 1975)') # Not a safe way to add rows

# Adding rows in a safe way using function
def safeMovieInsert(cur, title, year):
    cur.execute('INSERT INTO movies VALUES (?, ?)', (title, year))

safeMovieInsert(cur, 'Eternal Sunshine of the Spotless Mind', 2004)

# Reading rows from database
# Command_1: SELECT * FROM table_name
seq1 = cur.execute("SELECT * FROM movies") # It's a tuple not a list
# Command_2: SELECT table_columns FROM table_name
seq2 = cur.execute("SELECT title FROM movies")
# Command_3: SELECT * FROM table_name WHERE constraint
def moviesInYear(cur, year):
    r = cur.execute('SELECT * FROM movies WHERE year > (?)', (year))
    return r
seq3 = moviesInYear(cur, 2000)

for entry in seq3:
    print(entry)
    print(entry[0] + "\t" + str(entry[1]))

# Save changes by commiting
conn.commit()
# Close the connection
conn.close()
