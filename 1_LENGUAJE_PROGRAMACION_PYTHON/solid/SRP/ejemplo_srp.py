#Sin SRP
class User_Manager:
    def create_user(self, username, password):
        pass
    
    def update_user(self, username, new_password):
        pass
    
    def delete_user(self, username):
        pass
        
    def send_email(self, email):
        pass
    
    def log_activity(self, activity):
        pass


    
#Con SRP    
class User_Service:
    def create_user(self, username, password):
        pass
    
    def update_user(self, username, new_password):
        pass
    
    def delete_user(self, username):
        pass
    
class Email_Service:
    def send_email(self, email):
        pass
    
class Log_Service:
    def log_activity(self, activity):
        pass    
    
