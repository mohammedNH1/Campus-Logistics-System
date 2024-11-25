import re
class User:
    def __init__(self, ID , Fname , Lname , type, email , phone_number , password ):
        self.ID = ID
        self.Fname = Fname
        self.Lname = Lname
        self.type = type
        self.email = email
        self.phone_number = phone_number
        self.password = password
        
     


        
#mohammed = User(1, 1 , 1, 1, 1 ,"0500" , 1)
def input_valid(Fname ,Lname , Type , password, email ,  number,  id  ):
        valid_phone_number = re.search("^(05)" ,number)
        valid_ID = len(id) == 10
        valid_pass = len(password) >= 6
        valid_email = re.search("(@ksu.edu.sa)$", email)
        if not valid_phone_number:
             # error on GUI
             pass
        if not valid_ID:
             pass
        if not valid_pass:
             pass
        if not valid_email:
             pass
        mohammed = User(id , Fname , Lname , Type, email , number , password)


        

