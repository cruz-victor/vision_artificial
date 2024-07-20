#Ejemplo Metodos de pagos--------------------------------
#Sin OCP
class Payment_Processor:
    def process_payment(self, payment_type):
        if payment_type=="credit card":
            #Procesar pago con tarjeta de credito
            pass
        
        if payment_type=="paypal":
            #Procesar pago con paypal 
            pass

        #Mas metodos de pagos


#Con OCP        
#Interface
class Payment_Method:    
    def process_payment():
        pass

#Implement Interface    
class Creditcard_Payment(Payment_Method):
    def process_payment():
        #Procesar pago con tarjeta de credito
        pass            

#Implement Interface    
class Paypal_Payment(Payment_Method)    :
    def process_payment():
        #Procesar pago con paypal
        pass

#Inject component and method action
class Payment_Processor:
    def __init__(self, Payment_Method):
        self.__Payment_Method=Payment_Method    
        
    def process_payment(self):
        self.__Payment_Method.process_payment()    
                
                
                
#Ejemplo Notificaciones--------------------------------                
#Sin OCP
class Notification_Service:
    def send_notification(self, type):
        if type == "email":
            #enviar notificacion por email
            pass
        
        if type == "sms":
            #enviar notificacion por sms
            pass


#Con OCP
#Interface
class Notification:
    def send_notification(self):
        pass
    
#Implement Interface    
class Email_Notification(Notification)    :
    def send_notification(self):
        #Enviar notificacion por email
        pass
    
#Implement Interface    
class Sms_Notification(Notification):
    def send_notification(self):
        #Enviar notificacion por sms
        pass    
    
#Inject component and create method action
class Notification_Service:
    def __init__(self, Notification):
        self.__Notification=Notification
    
    def send_notification(self):
        self.__Notification.send_notification();

#Ejemplo Generacion de reportes--------------------------------                        
#Sin OCP
class Report_Generator:
    def generate_report(self, type):
        if type =="PDF":
            #Generar reporte de PDF
            pass
        
        if type == "Excel":
            #Generar reporte de excel
            pass
            
        if type == "Word":
            #Generar reporte word
            pass            

        
#Con OCP
#Interface
class Report:
    def generate_report(self):
        #Generar reporte
        pass

#Implement Interface        
class Pdf_Report(Report):
    def generate_report(self):
        #Generar reporte pdf
        pass            
    
#Implement Interface    
class Excel_Report(Report):
    def generate_report(self):
        #Generar reporte excel
        pass                

#Implement Interface
class Word_Report(Report):
    def generate_report(self):
        #Generar reporte word
        pass                    
    
#Inject component and create method action
class Report_Generator:
    def __init__(self, Report):
       self.__Report=Report

    def generate_report(self):
        self.__Report.generate_report()        