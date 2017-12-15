import re
import time

class Employee: 
    def __init__(self,empId,empName,empValidPhone,empValidEmail):
        self.empId = empId
        self.empName = empName
        self.empValidPhone = empValidPhone
        self.empValidEmail = empValidEmail
    
class Portal(Employee):
    database = {}

    def __init__(self):
        pass 
    
    def createEmployeeDetails(self):
        d = {}
        l = {}
        loop_id = False
        loop_phone = False
        loop_email = False
        
        while loop_id == False:
            empId = int(raw_input("Enter Employee Id:"))
            empValidId = ''
            if Portal.database.has_key(empId):
                print "Employee Id",empId,"Already Exists."
                time.sleep(2)
            else:
                empValidId  = empId
                loop_id = True
        empName = raw_input("Enter Employee Name:")
        l.update({"Name":empName})
        while loop_phone == False:
            empPhone = raw_input("Enter Employee Phone Number:")
            phoneObj = re.search(r'\d{3}-\d{3}-\d{4}',empPhone)
            empValidPhone = ''
            if phoneObj:
                empValidPhone = empPhone
                empValidPhone = self.checkPhoneValidation(empValidPhone)
                if empValidPhone == None:
                    print "Phone number",empPhone,"which you entered is already exists"
                else:
                    l.update({"Phone":empValidPhone})
                    loop_phone = True
            else:
                print "Please enter phone details as xxx-xxx-xxxx format"
        while loop_email == False:
            empEmail = raw_input("Enter Employee Email:")
            emailObj = re.search(r'[\w.]+@[\w.]+',empEmail)
            empValidEmail = ''
            if emailObj:
                empValidEmail = empEmail
                empValidEmail = self.checkEmailValidation(empValidEmail)
                if empValidEmail == None:
                    print "Email id",empEmail,"which you entered is already exists"
                else:
                    l.update({"Email":empValidEmail})
                    loop_email = True
            else:
                print "Please enter email details as xxx@xxx.xxx format"
           
        d.update({empValidId:l})
        Portal.database.update(d)
        
    def updateEmployeeDetails(self):
        loop = False
        if not Portal.database.items():
            print "\nNo records found. First you create employee details"
            time.sleep(2)
            print "\nProcess for creating new employee"
            time.sleep(2)
            self.createEmployeeDetails()
            print "Employee created successfully"
            time.sleep(2)
        print "Employee Id List: ",Portal.database.keys()
        print "\nNow process for update employee details"
        time.sleep(2)
        while loop == False:
            num = int(raw_input("Enter employee id which you want to update: "))
            if Portal.database.has_key(num):
                self.selectOption(num)
                print "Employee details updated successfully"
                time.sleep(2)
                print '\nNow select option for another process'
                loop =True
            else:
                print "Employee Id",num,"doesn't exists in employee id list",Portal.database.keys()
    
    def selectOption(self,num):
        loop_phone_data = False
        loop_email_data = False
        record = Portal.database.get(num)
        print '''Choose option to update :
        Name
        Phone
        Email
        '''
        print "\nNOTE: Please select option as per format like option1,option2,option3,etc..."
        option = (raw_input("Enter Options :")).split(',')
        for i in option:
            if i == "name" or i == "Name":
                name = raw_input("Enter name which you want to update:")
                record.update({'Name':name})
            elif i == "phone" or i == "Phone":
                while loop_phone_data == False:
                    phone = raw_input("Enter phone which you want to update:")
                    phoneData = re.search(r'\d{3}-\d{3}-\d{4}',phone)
                    empValidPhoneData = ''
                    if phoneData:
                        empValidPhoneData = phone
                        empValidPhoneData = self.checkPhoneValidation(empValidPhoneData)
                        if empValidPhoneData == None:
                            print "Phone number",phone,"which you entered is already exists"
                        else:
                            record.update({'Phone':empValidPhoneData})
                            loop_phone_data = True
                    else:
                        print "Please enter phone details as xxx-xxx-xxxx format"
            elif i == "email" or i == "Email":
                while loop_email_data == False:
                    email = raw_input("Enter email which you want to update:")
                    emailData = re.search(r'[\w.]+@[\w.]+',email)
                    empValidEmailData = ''
                    if emailData:
                        empValidEmailData = email
                        empValidEmailData = self.checkEmailValidation(empValidEmailData)
                        if empValidEmailData == None:
                            print "Email id",email,"which you entered is already exists"
                        else:
                            record.update({'Email':empValidEmailData})
                            loop_email_data = True
                    else:
                        print "Please enter email details as xxx@xxx.xxx format"
            else:
                print "Select valid options"
                time.sleep(2)
                return self.selectOption(num)
    
    def printAllEmployee(self,database):
        if not Portal.database.items():
            print "No Any Records Available, Please Create Employee Details"
        else:
            print "All Employee Details:",database
        time.sleep(2)
        
    def deleteEmployeeDetails(self):
        loop_data = False
        if not Portal.database.items():
            print "\nNo records found. First you create employee details"
            time.sleep(2)
            print "\nProcess for creating new employee"
            time.sleep(2)
            self.createEmployeeDetails()
            print "Employee created successfully"
            time.sleep(2)
            print "\nNow Process for delete existing employee record"
        while loop_data == False:
            data = int(raw_input('Enter employee id:'))
            if Portal.database.has_key(data):
                Portal.database.pop(data)
                print "Employee id",data,"deleted successfully"
                loop_data = True
            else:
                print "No record found"
    
    def checkPhoneValidation(self,empValidPhone):
        record = {}
        list1 = []
        phone = None
        data = Portal.database.values()
        for data1 in data:
            record.update(data1)
            if record.has_key("Phone"):
                list1.append(record.get("Phone"))
        if empValidPhone not in list1:
            #print "Phone which you entered is valid"
            phone = empValidPhone
            return phone
        else:
            return phone   
     
    def checkEmailValidation(self,empValidEmail):
        record = {}
        list1 = []
        email = None
        data = Portal.database.values()
        for data1 in data:
            record.update(data1)
            if record.has_key("Email"):
                list1.append(record.get("Email"))
        if empValidEmail not in list1:
            #print "Phone which you entered is valid"
            email = empValidEmail
            return email
        else:
            return email         
            