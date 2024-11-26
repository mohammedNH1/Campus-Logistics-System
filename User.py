import re
from DataBase import database
import hashlib
class user:
    
    def __init__(self, ID , Fname , Lname , Type, email , phone_number , password ):
        self.ID = ID
        self.Fname = Fname
        self.Lname = Lname
        self.Type = Type
        self.email = email
        self.phone_number = phone_number
        self.password = hashlib.sha256(password.encode()).hexdigest()
        DB = database()
        DB.insertUser(self.ID , self.Fname , self.Lname , self.Type , self.email , self.phone_number , self.password )
        

        
     


        
#mohammed = User("44410", "Mohammed" , "alhassan", "Student", "mohammedcom" , 324023140 , "123456")



        

