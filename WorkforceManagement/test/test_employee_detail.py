from django.test import TestCase
from django.urls import reverse
from WorkforceManagement.models import Employee, Department, Computer, Training_Prog

"""
Class Employee Detail Test was created to test on whether an instatiated user passes the proper Status, Context, & Content
Author: Jacob Smith && Cashew Rose

"""
class Employee_Detail_Test(TestCase):

    """
    The setup class creates 4 instances, one of each of our models to see if Employee can pass the proper tests

    """
    def setUp(self):
        self.new_department = Department.objects.create(
            dept_name='Accounting',
            budget=50
        )

        self.new_computer = Computer.objects.create(
            purchase_date='2018-08-08',
            decom_date='2023-08-08',
            manufacturer='Macbook',
            make='Pro 15in',
            has_been_assigned='False'
        )

        self.new_training = Training_Prog.objects.create(
            prog_name='Jazzercise 101',
            training_desc='Get ready to get Jazzy with it',
            start_date='2018-08-08',
            end_date='2018-08-10',
            max_attendance='50'
        )

        self.new_employee = Employee.objects.create(
            department=self.new_department,
            computer=self.new_computer,
            is_supervisor=False,
            name='Jacob Smith',
            start_date='2018-08-08'
        )
    
        """
        When adding an item with a ManyToManyField, like training, you can't store the training directly on employee.
            Adding the new_training, like below, satisfies the many to many relationship.
        Author: Jacob Smith && Cashew Rose
        """
        self.new_employee.training.add(self.new_training)

        """
        Response will store the returned url information to test against. 
            This response is checking the one instance being made in kwargs (DetailView must have an arguement passed this way in test suite)
        """
        self.response = self.client.get(reverse('employee_detail', kwargs={'pk':1}))


    # ========== TESTING ==========


    def test_Employee_Detail_Url_Exists(self):

        """
        Test that checks to see if the response returns that it can be found. Thats what the 200 status code is
        """
        self.assertEqual(self.response.status_code, 200)

    def test_Employee_Detail_Model_In_View(self):
        
        """
        Test that checks to see if the employee detail content of the response has all of the expected values of the employee for each of the properties
        """
        self.assertIn(self.new_employee.name.encode(), self.response.content)

        """
        Test that checks to see if the employee detail content of the response has all of the expected values of the employee for each of the properties
            ¯\_(ツ)_/¯ Foreign key tests must be formatted in funky unicode and then encoded ¯\_(ツ)_/¯
        """
        self.assertIn(u'{}'.format(self.new_employee.computer).encode(), self.response.content)
        self.assertIn(u'{}'.format(self.new_employee.department).encode(), self.response.content)
        
        """
        Test that checks to see if the employee detail content of the response has all of the expected values of the employee for each of the properties
            For a ManyToManyField you have to check one of the primary keys in that many table with the other table to make sure they match
            ¯\_(ツ)_/¯
        """
        self.assertEqual(self.new_employee.training.get(pk=self.new_training.pk), self.new_training)

    def test_Employee_Detail_Object_In_View(self):

        """
        Test that checks to see if the whole employee object has made it into the response context
        """
        self.assertEqual(self.new_employee, self.response.context['object'])
