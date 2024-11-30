import sqlite3
import csv

class database:
    def __init__(self):
        self.conn = sqlite3.connect('dataBase.db')
        self.cursor = self.conn.cursor()

    def initiate_database(self):
        conn = sqlite3.connect('dataBase.db')
        conn.execute('''CREATE TABLE USER
        (ID TEXT PRIMARY KEY NOT NULL,
        F_NAME TEXT NOT NULL,
        L_NAME TEXT NOT NULL,
        TYPE TEXT NOT NULL,
        EMAIL TEXT NOT NULL,                 
        PHONE_NUMBER TEXT NOT NULL,
        PASSWORD TEXT NOT NULL);''')
        print("USER Table created successfully")

        conn.execute('''CREATE TABLE OFFICE
        (ID TEXT PRIMARY KEY NOT NULL,        
        NAME TEXT NOT NULL   
        );''')
        print("OFFICE Table created successfully")

        conn.execute('''CREATE TABLE PACKAGE
        (TRACKING_NUMBER TEXT PRIMARY KEY NOT NULL,
        OFFICE_ID TEXT NOT NULL,
        RECEIVER_ID TEXT NOT NULL,
        SENDER_ID TEXT NOT NULL,                 
        DIMENSIONS TEXT NOT NULL,
        WEIGHT REAL NOT NULL,
        STATUS TEXT NOT NULL, 
        FOREIGN KEY (OFFICE_ID) REFERENCES OFFICE(ID) ON DELETE CASCADE,
        FOREIGN KEY (RECEIVER_ID) REFERENCES USER(ID) ON DELETE CASCADE,
        FOREIGN KEY (SENDER_ID) REFERENCES USER(ID) ON DELETE CASCADE
        );''')
        print("PACKAGE Table created successfully")

        conn.close()
    def insertUser(self , id , FNAME , LNAME , Type , email , phone_number , password):
        conn = sqlite3.connect('dataBase.db')
        
        query = '''INSERT INTO USER (ID, F_NAME, L_NAME, TYPE, EMAIL, PHONE_NUMBER, PASSWORD)
                   VALUES (?, ?, ?, ?, ?, ?, ?)'''
        
        conn.execute(query, (id, FNAME, LNAME, Type, email, phone_number, password))
        conn.commit()
        conn.close()
        
    def retrieveUser(self, id, password):
        mySet = {"Student","Faculty"}
        
        cursor = self.conn.execute("SELECT ID, TYPE, PASSWORD from USER")  

        for row in cursor:
            if id == row[0] and password == row[2]: 
                if row[1] in mySet:
                    return True 
                else:
                    return "Courier"  
        
        self.conn.close() 
        return False  
    
    def insertOffice(self , id , name):
        try:
            conn = sqlite3.connect('dataBase.db')
            
            query = '''INSERT INTO OFFICE (ID, NAME)
                    VALUES (?, ?)'''
            
            conn.execute(query, (id, name))
            conn.commit()
            conn.close()
        except:
            print("office already exist")   

    def insertPackage(self , tracking_number , office_id , receiver_id , sender_id , dimensions , weight , status):
      
            conn = sqlite3.connect('dataBase.db')
            
            query = '''INSERT INTO PACKAGE (TRACKING_NUMBER, OFFICE_ID ,RECEIVER_ID , SENDER_ID ,DIMENSIONS, WEIGHT , STATUS )
                    VALUES (?, ?, ? , ? , ?, ?, ? )'''
            
            conn.execute(query, (tracking_number, office_id , receiver_id , sender_id , dimensions , weight , status ))
            conn.commit()
            conn.close()
    def retrieveOffices(self):
        cursor = self.conn.execute("SELECT ID , NAME  from OFFICE")  
        diction = {}
        for row in cursor:
            diction[row[1]] = row[0]
        
        self.conn.close() 
        return diction
    
    def retrievePackages(self):
        
        cursor = self.conn.execute("SELECT TRACKING_NUMBER , OFFICE_ID, RECEIVER_ID, SENDER_ID , DIMENSIONS , WEIGHT , STATUS from PACKAGE")  
        main_list = []
        
        for row in cursor: 
            current_list = []
            current_list.append(row[0])
            current_list.append(row[1])
            current_list.append(row[2])
            current_list.append(row[3])
            current_list.append(row[4])
            current_list.append(row[5])
            current_list.append(row[6])
            main_list.append(current_list)
        
        self.conn.close() 
        
        return main_list 
    def update_status(self, status ,tracking_number ):
        try:
           
           
            self.conn.execute("UPDATE PACKAGE SET STATUS = ? WHERE TRACKING_NUMBER = ?", (status , tracking_number))
            self.conn.commit()
        except Exception as e:
            print(f"Error updating status: {e}")
                
    def backup(self):
        file = open("backup.csv" , "w" , newline="")
        writer = csv.writer(file)
        cursor = self.conn.execute("SELECT * from USER")  

        writer.writerow(["ID", "First Name", "Last Name", "Type", "Email", "Phone Number", "Password"] )
        for i in cursor:
            writer.writerow(i)

        cursor = self.conn.execute("SELECT * from OFFICE")
        writer.writerow(["ID","Name"])    
        for i in cursor:
            writer.writerow(i)

        cursor = self.conn.execute("SELECT * from PACKAGE")
        writer.writerow(["Tracking Number","Office ID" , "Receiver ID" , "Sender ID" , "Weight" , "Status"]) 
        for i in cursor:
            writer.writerow(i)





 

# mohammed = database()
# mohammed.initiate_database()

