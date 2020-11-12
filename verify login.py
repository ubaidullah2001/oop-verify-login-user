class user:
    def __init__(self,user_id,password):
        self.user_id = user_id
        self.password = password
        self.loginStatus=False
        self.users=['burhan','yousuf','obaid']
        self.passwordList=[123,456,789]
    def verifyLogin(self):
        for i in range(len(self.users)):
            if (self.users[i]==self.user_id and self.passwordList[i]==self.password):
                self.loginStatus=True
        return self.loginStatus
a=user('yousuf',456)
print(a.verifyLogin())    

        
class customer:
    def __init__(self,c_name,address,email,credit_card,shipping_info):
          self.c_name = c_name
          self.address = address
          self.email = email
          self.credit_card = credit_card
          self.shipping_info = shipping_info



          
class admin:
    def __init__(self,admin_name,email):
        self.admin_name = admin_name
        self.email = email
        
        
       
        