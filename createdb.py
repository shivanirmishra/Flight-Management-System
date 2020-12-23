import sqlite3

conn = sqlite3.connect('hola.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE ECONOMY
         (ADHAR INT(4) CHECK (ADHAR>999 AND ADHAR<10000),
         NAME           TEXT    NOT NULL,
         SOURCE           CHAR(50),
         DESTINATION        CHAR(50),
         DATE       CHAR(50),
         TIME        CHAR(50)
         );''')
print("Table created successfully")

conn.execute('''CREATE TABLE BUSINESS
         (ADHAR INT(4) CHECK (ADHAR>999 AND ADHAR<10000),
         NAME           TEXT    NOT NULL,
         SOURCE           CHAR(50),
         DESTINATION        CHAR(50),
         DATE       CHAR(50),
         TIME        CHAR(50)
         );''')
print("Table created successfully")

conn.execute('''CREATE TABLE FIRST
         (ADHAR INT(4) CHECK (ADHAR>999 AND ADHAR<10000),
         NAME           TEXT    NOT NULL,
         SOURCE           CHAR(50),
         DESTINATION        CHAR(50),
         DATE       CHAR(50),
         TIME        CHAR(50)
         );''')
print("Table created successfully")

conn.execute('''CREATE TABLE ECONOMY1
         (ADHAR INT(4) CHECK (ADHAR>999 AND ADHAR<10000),
         NAME           TEXT    NOT NULL,
         SOURCE           CHAR(50),
         DESTINATION        CHAR(50),
         DATE       CHAR(50),
         TIME        CHAR(50),
         RETURNDATE       CHAR(50),
         RETURNTIME        CHAR(50)
         );''')
print("Table created successfully")

conn.execute('''CREATE TABLE BUSINESS1
         (ADHAR INT(4) CHECK (ADHAR>999 AND ADHAR<10000),
         NAME           TEXT    NOT NULL,
         SOURCE           CHAR(50),
         DESTINATION        CHAR(50),
         DATE       CHAR(50),
         TIME        CHAR(50),
         RETURNDATE       CHAR(50),
         RETURNTIME        CHAR(50)
         );''')
print("Table created successfully")

conn.execute('''CREATE TABLE FIRST1
         (ADHAR INT(4) CHECK (ADHAR>999 AND ADHAR<10000),
         NAME           TEXT    NOT NULL,
         SOURCE           CHAR(50),
         DESTINATION        CHAR(50),
         DATE       CHAR(50),
         TIME        CHAR(50),
         RETURNDATE       CHAR(50),
         RETURNTIME        CHAR(50)
         );''')
print("Table created successfully")

conn.execute('''CREATE TABLE FLIGHT
         (SOURCE           CHAR(50),
         DESTINATION        CHAR(50),
         FID       CHAR(50),
         DATE       CHAR(50),
         TIME         CHAR(50),
         STATUS       CHAR(50));''')
print("Table created successfully")

