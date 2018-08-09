from django.test import TestCase
from django.urls import reverse
from WorkforceManagement.models import Employee_Model, Department_Model, Computer_Model, Training_Model

class Employee_Detail_Test(TestCase):
    """
    Class Employee Test was created to test on whether an instatiated user passes the proper Status, Context, & Content
    Author: Jacob Smith

    Arguments:
    Has one function named test_list_employee with four variables: new_department, new_computer, new_training, new_employee
    """
    # def setUpTestData(self):
    def test_list_employee(self):
        """
        test_list_employee has four variables that create instances of our models to see if Employee can pass the proper tests

        """
        new_department = Department_Model.Department.objects.create(
            dept_name='Accounting',
            budget=50
        )
        new_computer = Computer_Model.Computer.objects.create(
            purchase_date='2018-08-08',
            decom_date='2023-08-08',
            manufacturer='Macbook',
            make='Pro 15in',
            has_been_assigned='True'
        )
        new_training = Training_Model.Training_Prog.objects.create(
            prog_name='Jazzercise 101',
            training_desc='Get ready to get Jazzy with it',
            start_date='2018-08-08',
            end_date='2018-08-10',
            max_attendance='50'
        )
        new_employee = Employee_Model.Employee.objects.create(
            department=new_department,
            computer=new_computer,
            is_supervisor=False,
            name='Jacob Smith',
            start_date='2018-08-08'
        )
        """
        When adding an item with a ManyToManyField on, like training. When creating the instance of new employee, don't store the training directly on employee.
        Adding the new_training, like below, satisfies the many to many relationship.
        Author: Jacob Smith && Cashew Rose
        """
        new_employee.training.add(new_training)


    # ========== TESTING ==========
        """
        Response will store the returned url information to test against. 
            This response is checking the one instance being made in kwargs (DetailView must have an arguement passed this way in test suite)
        """
        response = self.client.get(reverse('employee_detail', kwargs={'pk':1}))

        """
        Test that checks to see if the response returns that it can be found. Thats what the 200 status code is
        """
        self.assertEqual(response.status_code, 200)

        """
        Test that checks to see if the employee detail content of the response has all of the expected values of the employee for each of the properties
        """
        self.assertIn(new_employee.name.encode(), response.content)

        """
        Test that checks to see if the employee detail content of the response has all of the expected values of the employee for each of the properties
            Foreign key tests must be formatted in funky unicode and then encoded ¯\_(ツ)_/¯
        """
        self.assertIn(u'{}'.format(new_employee.computer).encode(), response.content)
        self.assertIn(u'{}'.format(new_employee.department).encode(), response.content)
        self.assertIn(new_employee.training, response.content)

        """
        Test that checks to see if the whole employee object has made it into the response context
        """
        self.assertEqual(new_employee, response.context['object'])