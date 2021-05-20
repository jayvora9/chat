import sqlite3
from sqlite3 import Error
from random import randint

def create_conn(db_file):
     try:
         conn = sqlite3.connect(db_file)
     except Error as e:
         print(e)
     finally:
         conn.close()

conn = sqlite3.connect('db\\sqlite\\db\\pythonsqlite.db')

c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")


def create_tables(c):
    try:

        c.execute('CREATE TABLE IF NOT EXISTS LOGIN'
                  '(id integer PRIMARY KEY NOT NULL, '
                  'email text, '
                  'pswd text)');

        c.execute('CREATE TABLE IF NOT EXISTS STUD_INFO'
                  '(id integer PRIMARY KEY NOT NULL, '
                  'fname text, '
                  'lname text, '
                  'sem_id integer, '
                  'FOREIGN KEY(id) REFERENCES LOGIN(id) ON DELETE CASCADE)');

        c.execute('CREATE TABLE IF NOT EXISTS GPA_DETAILS'
                  '(id integer, '
                  'sem1 real, '
                  'sem2 real, '
                  'sem3 real, '
                  'sem4 real, '
                  'sem5 real, '
                  'sem6 real, '
                  'sem7 real, '
                  'sem8 real, '
                  'FOREIGN KEY(id) REFERENCES STUD_INFO(id) ON DELETE CASCADE)');

    except Error as e:
        print(e)


create_tables(c)
conn.commit()


def populate(c):
    try:
        # id, email, pswd


        LOGIN_INFO = [(1, 'jay.vora@sakec.ac.in', 'jay'),
                       (2, 'gunjan.vora@sakec.ac.in', 'gunjan'),
                       (3, 'kaushik.gami@sakec.ac.in', 'kaushik'),
                       (4, 'keval.shah@sakec.ac.in', 'keval'),
                      (5, 'rutvi.shah@sakec.ac.in', 'rutvi'),
                      (6, 'siddhi.rane@sakec.ac.in', 'siddhi'),
                      (7, 'aarohi@sakec.ac.in', 'aaroho'),
                      (8, 'shrushti@sakec.ac.in', 'shrushti'),
                      (9, 'kulkarnir@sakec.ac.in', 'kulkarnir'),
                      (10, 'agrawals@sakec.ac.in', 'agrawals'),
                      (11, 'rathorea@sakec.ac.in', 'rathorea'),
                      (12, 'lahotir@sakec.ac.in', 'lahotir')]

        c.executemany('INSERT INTO LOGIN VALUES (?,?,?)', LOGIN_INFO)

        # id, fname, lname, sem_id


        STUD_DETAILS = [(1, 'jay', 'vora', 6),
                         (2, 'Gunjan', 'Vora', 7),
                         (3, 'Kaushik', 'Gami', 8),
                         (4, 'Keval', 'Shah', 6),
                        (5, 'Rutvi', 'Shah', 7),
                        (6, 'Siddhi', 'rane', 8),
                        (7, 'Aaroho', 'Uthale', 8),
                        (8, 'shrushti', 'gada', 3),
                        (9, 'Ram', 'Kulkarni', 2),
                        (10, 'Shantanu', 'Agrawal', 3),
                        (11, 'Aman', 'Rathore', 5),
                        (12, 'Radhika', 'Lahoti', 6)]

        c.executemany('INSERT INTO STUD_INFO VALUES (?,?,?,?)', STUD_DETAILS)

        # id, sem(1 to 8)


        GPA_DETAILS = [(1, 8.9 , 8.3 , 8.6 , 8.5 , 8.4 , 0.0 , 0.0 , 0.0),
                       (2, 8.9 , 8.3 , 8.6 , 8.5 , 8.4 , 8.9 , 0.0 , 0.0),
                       (3, 8.9 , 8.3 , 8.6 , 8.5 , 8.4 , 8.5 , 9.2 , 0.0),
                       (4, 8.9, 8.3, 8.6, 8.5, 8.4, 0.0, 0.0, 0.0),
                       (5, 8.6, 8.3, 9.0, 8.5, 8.4, 8.9, 0.0, 0.0),
                       (6, 8.4, 8.3, 9.4, 8.9, 8.8, 9.5, 9.2, 0.0),
                       (7, 8.4, 8.3, 7.9, 8.5, 8.4, 8.9, 9.0, 0.0),
                       (8, 8.0, 8.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                       (9, 8.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                       (10, 8.1, 8.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                       (11, 8.7, 8.7, 8.6, 8.5, 0.0, 0.0, 0.0, 0.0),
                       (12, 8.9, 8.7, 8.6, 8.5, 8.1, 0.0, 0.0, 0.0)
                       ]

        c.executemany('INSERT INTO GPA_DETAILS VALUES (?,?,?,?,?,?,?,?,?)', GPA_DETAILS);

    except Error as e:
        print(e)


populate(c)
conn.commit()


def bulkDataIns():
   print("DATA INSERTED")
   for num in range(13,150):
        # if (num%2)==0:
            c.execute( "INSERT INTO LOGIN VALUES(?,?,?)",(num,'abc'+str(num)+'@sakec.ac.in','abc'+str(num)) )
            # c.execute( "INSERT INTO STUD_INFO VALUES(?,?,?,?)", () )
        # else:
        #     c.execute("INSERT INTO LOGIN VALUES(?,?,?)",(num,'xyz'+str(num)+'@sakec.ac.in','xyz'+str(num)) )
for num in range(13, 201):
    # if (num % 2) == 0:
    
              c.execute("INSERT INTO LOGIN VALUES(?,?,?)", (num, 'abc' + str(num) + '@sakec.ac.in', 'abc' + str(num)))
              c.execute( "INSERT INTO STUD_INFO VALUES(?,?,?,?)", (num, 'ABC' , 'DEF' , 8) )
              c.execute("INSERT INTO GPA_DETAILS VALUES(?,?,?,?,?,?,?,?,?)", (num, 8.4, 8.3, 9.4, 8.9, 8.8, 9.5, 9.2, 0.0))
    # else:
    #           c.execute("INSERT INTO LOGIN VALUES(?,?,?)", (num, 'xyz' + str(num) + '@sakec.ac.in', 'xyz' + str(num)))
    #           c.execute("INSERT INTO STUD_INFO VALUES(?,?,?,?)", (num, 'PQR', 'XYZ', 7))
    
    #           c.execute("INSERT INTO GPA_DETAILS VALUES(?,?,?,?,?,?,?,?,?)", (num, 8.6, 8.3, 9.0, 8.5, 8.4, 8.9, 0.0, 0.0))


bulkDataIns()
conn.commit()


for num in range(13,15):
         print(num,'abc'+str(num)+'@sakec.ac.in','abc'+str(num))
