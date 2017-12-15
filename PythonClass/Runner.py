import ClassDemo
import sys
import time

class Runner:
    def employeeOpration(self,portal_obj):
        loop = False
        print '''Employee Details:
        1) Create Employee
        2) Update Employee
        3) Print All Employee
        4) Delete Employee
        5) Exit the program
        '''
        while loop == False:
            option = raw_input("Please Select any option : ")
            if option.isdigit():
                op = int(option)
                if op == 1: 
                    print "\nYou select option",option,", Now Process for creating new employee details"
                    time.sleep(2)
                    portal_obj.createEmployeeDetails()
                    time.sleep(2)
                    print 'Employee details created successfully'
                    time.sleep(2)
                    print ''
                    print 'Now choose any option for another process'
                    time.sleep(2)
                    self.employeeOpration(portal_obj)
                elif op == 2:
                    print "\nYou select option",option,", Now Process for updating existing employee details"
                    time.sleep(3)
                    portal_obj.updateEmployeeDetails()
                    self.employeeOpration(portal_obj)
                elif op == 3:
                    print "\nYou select option",option,", Now Process for getting all employee with details"
                    time.sleep(3)
                    portal_obj.printAllEmployee(portal_obj.database)
                    print '\nNow choose any option for another process'
                    self.employeeOpration(portal_obj)
                elif op == 4:
                    print "\nYou select option",option,", Now Process for deleting employee details"
                    time.sleep(2)
                    portal_obj.deleteEmployeeDetails()
                    time.sleep(2)
                    print '\nNow choose any option for another process'
                    self.employeeOpration(portal_obj)
                elif op == 5:
                    print "Successfully exit from Application. Thanking You...!!!"
                    sys.exit()
                else:
                    print "\nYou select option",option,"is invalid. Please choose valid option"
                    time.sleep(2)
                    return self.employeeOpration(portal_obj)
                loop = True
            else:
                print "Please enter value as digit like 1,2,3,...."
        
portal_obj = ClassDemo.Portal()
runner_obj = Runner().employeeOpration(portal_obj)