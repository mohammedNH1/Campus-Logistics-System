import sqlite3

class database:
    def __init__(self):
        self.conn = sqlite3.connect('dataBase.db')
        self.cursor = self.conn.cursor()

    def initiate_database(self):
        conn = sqlite3.connect('dataBase.db')
        conn.execute('''CREATE TABLE USER
        (ID INT PRIMARY KEY NOT NULL,
        F_NAME TEXT NOT NULL,
        L_NAME TEXT NOT NULL,
        TYPE TEXT NOT NULL,
        EMAIL TEXT NOT NULL,                 
        PHONE_NUMBER TEXT NOT NULL,
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
    def insertUser(self , id , FNAME , LNAME , Type , email , phone_number , password):
        conn = sqlite3.connect('dataBase.db')
        
        # Use a parameterized query to avoid SQL injection and errors with string values
        query = '''INSERT INTO USER (ID, F_NAME, L_NAME, TYPE, EMAIL, PHONE_NUMBER, PASSWORD)
                   VALUES (?, ?, ?, ?, ?, ?, ?)'''
        
        # Execute the query with parameters passed as a tuple
        conn.execute(query, (id, FNAME, LNAME, Type, email, phone_number, password))
        conn.commit()
        conn.close()
        #ds


