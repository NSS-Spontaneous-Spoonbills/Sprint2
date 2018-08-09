from django.test import TestCase, Client
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
        Author: Jacob Smith
        """
        new_employee.training.add(new_training)

    # ========== TESTING ==========
        """
        Response will store our url and represent fetching this list
        """
        response = self.client.get(reverse('Employee_List'))

        """
        Test that checks to see if the response returns an actual item, and that it can be found. Hence the 200 status code
        """
        self.assertEqual(response.status_code, 200)

        """
        Test that checks to see if the employee list returns only one item. It is the one object we created & stored in the new_employee variable
        """
        self.assertEqual(len(response.context['Employee_List']), 1)
        """
        This test checks if the encoded variable is written in python
        """
        self.assertIn(new_employee.name.encode(), response.content)


class Computer_Test(TestCase):
    """Tests computer functionality for WorkforceManagement
    Author: Erin Meaker
    """

    def test_list_computer(self):
        """Tests will build two testing computers to ascertain the following:

        Author: Erin Meaker
        """
        assigned_Computer = Computer_Model.Computer.objects.create(
            purchase_date='2018-01-01',
            decom_date=None,
            manufacturer='Dell',
            make='Spider Nest',
            has_been_assigned='1'
        )
        unassigned_Computer = Computer_Model.Computer.objects.create(
            purchase_date='2018-01-01',
            decom_date=None,
            manufacturer='Apple',
            make='Orange',
            has_been_assigned='0'
        )
        c = Client()

        # Testing

        response = c.get('computers', {'purchase_date': '2018-01-01', 'decom_date': None,
                                       'manufacturer': 'Dell', 'make': 'Spider Nest', 'has_been_assigned': '1'})

        self.assertEqual(response, 'computers', kwargs={'pk': 1})
