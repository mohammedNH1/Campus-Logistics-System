import sqlite3
class DataBase:
    def __init__(self):
        pass
    conn = sqlite3.connect('dataBase.db')
    conn.execute('''CREATE TABLE User
    (ID INT PRIMARY KEY NOT NULL,
    Fname TEXT NOT NULL,
    Lname TEXT NOT NULL,
    Type TEXT NOT NULL,
    Email TEXT NOT NULL,                 
    Phone_Number INT NOT NULL,
    Password TEXT NOT NULL);''')
    print ("Table created successfully")
    conn.execute('''CREATE TABLE Package
    (ID INT PRIMARY KEY NOT NULL,
    office_id INT NOT NULL,
    recieverID INT NOT NULL,
    senderID INT NOT NULL,
    tracking_number TEXT NOT NULL,                 
    dimenstions TEXT NOT NULL,
    weight REAL NOT NULL,
    FOREIGN KEY (office_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (reciever_id) REFERENCES User(id) ON DELETE CASCADE             
    FOREIGN KEY (sender_id) REFERENCES users(id) ON DELETE CASCADE             
                      
                 );''')
    conn.close()



