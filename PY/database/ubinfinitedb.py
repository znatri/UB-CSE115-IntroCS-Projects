import sqlite3
import csv

conn = sqlite3.connect("file2.db")

cur = conn.cursor()

# def add_record(strOne, strTwo, strThree):
#     cur.execute("INSERT INTO blond VALUES (?, ?, ?)", (strOne, strTwo, strThree))
#     conn.commit()

# def get_records():
#     records = list(cur.execute("SELECT * FROM stare"))
#     return records

# def create_table():
#     cur.execute("CREATE TABLE IF NOT EXISTS muscle (tricep, biceps, abs)")

# def add_list(listArr):
#     for row in listArr:
#         cur.execute("INSERT INTO offer VALUES (?, ?, ?)", (row[0], row[1], row[2]))
#     conn.commit()

# def csv_to_db(csvfilename):
#     with open(csvfilename) as f:
#         reader = csv.reader(f)
#         for record in reader:
#             cur.execute("INSERT INTO farm VALUES (?, ?, ?)", (record[0], record[1], record[2]))
#     conn.commit()
       
# def filtered_records():
#     records = list(cur.execute("SELECT * FROM intense WHERE stop > 40"))
#     return records

conn.close()