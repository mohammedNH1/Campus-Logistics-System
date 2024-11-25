import sqlite3

class DataBase:
    def __init__(self):
        pass

    def initiate_database(self):
        conn = sqlite3.connect('dataBase.db')

        conn.execute('''CREATE TABLE USER
        (ID INT PRIMARY KEY NOT NULL,
        F_NAME TEXT NOT NULL,
        L_NAME TEXT NOT NULL,
        TYPE TEXT NOT NULL,
        EMAIL TEXT NOT NULL,                 
        PHONE_NUMBER INT NOT NULL,
        PASSWORD TEXT NOT NULL);''')
        print("USER Table created successfully")

        conn.execute('''CREATE TABLE OFFICE
        (ID INT PRIMARY KEY NOT NULL,        
        NAME TEXT NOT NULL   
        );''')
        print("OFFICE Table created successfully")

        conn.execute('''CREATE TABLE PACKAGE
        (ID INT PRIMARY KEY NOT NULL,
        OFFICE_ID INT NOT NULL,
        RECEIVER_ID INT NOT NULL,
        SENDER_ID INT NOT NULL,
        TRACKING_NUMBER TEXT NOT NULL,                 
        DIMENSIONS TEXT NOT NULL,
        WEIGHT REAL NOT NULL,
        FOREIGN KEY (OFFICE_ID) REFERENCES OFFICE(ID) ON DELETE CASCADE,
        FOREIGN KEY (RECEIVER_ID) REFERENCES USER(ID) ON DELETE CASCADE,
        FOREIGN KEY (SENDER_ID) REFERENCES USER(ID) ON DELETE CASCADE
        );''')
        print("PACKAGE Table created successfully")

        conn.close()

db = DataBase()
db.initiate_database()
