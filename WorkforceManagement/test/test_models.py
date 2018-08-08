from django.test import TestCase
from django.urls import reverse
from WorkforceManagement.models import Employee_Model, Department_Model, Computer_Model, Training_Model

class Employee_Test(TestCase):
"""
Class Employee Test was created to test on whether an instatiated user passes the proper Status, Context, & Content
Author: Jacob Smith

Arguments:
    Has one function named test_list_employee with four variables: new_department, new_computer, new_training, new_employee
"""
    # def setUpTestData(self):
    def test_list_employee(self):
        """
        test_list_employee has four variables that create instances of our models to test if Employee can pass the proper tests


        """
        new_department = Department_Model.Department.objects.create(
            dept_name='Accounting',
            budget=50
        )
        new_computer = Computer_Model.Computer.objects.create(
            purchase_date='08/08/2018',
            decom_date='08/08/2023',
            manufacturer='Macbook',
            make='Pro 15in'
        )
        new_training = Training_Model.Training_Prog.objects.create(
            prog_name='Jazzercise 101',
            training_desc='Get ready to get Jazzy with it',
            start_date='08/10/2018',
            end_date='08/11/2018',
            max_attendance='50'
        )
        new_employee = Employee_Model.Employee.objects.create(
            department=new_department,
            computer=new_computer,
            is_supervisor=False,
            name='Jacob Smith',
            start_date='08/08/2018'
        )
        new_employee.training.add(new_training)


    # ========== TESTING ==========
        """
        response stores the url
        """
        response = self.client.get(reverse('Employee_List'))

        """
        Test that checks to see if the response returns an actual item, and that it can be found. Hence the 200 status code
        """
        self.assertEqual(response.status_code, 200)

        """
        Test that checks to see if the employee list returns only on item. It is the one object we created stored in the new_employee variable
        """
        self.assertEqual(len(response.context['Employee_List']), 1)
        """
        This test does something that I need to create a better docstring for
        """
        self.assertIn(new_employee.name.encode(), response.content)