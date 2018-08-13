from django.test import TestCase
from django.urls import reverse
from WorkforceManagement.models import Computer_Model


class Computer_Test(TestCase):
    """Tests computer functionality for WorkforceManagement
    Author: Erin Meaker
    """

    def setUp(self):
        """Tests will build two testing computers to ascertain the following:

        Author: Erin Meaker
        """
        self.assigned_Computer = Computer_Model.Computer.objects.create(
            purchase_date='2018-01-01',
            decom_date=None,
            manufacturer='Dell',
            make='Spider Nest',
            has_been_assigned='1'
        )
        self.unassigned_Computer = Computer_Model.Computer.objects.create(
            purchase_date='2018-01-01',
            decom_date=None,
            manufacturer='Apple',
            make='Orange',
            has_been_assigned='0'
        )

        """ass_response refers to the object returned when pulling an "assigned computer" from the data above. It is not a fart.
        Likewise, "unass_response" refers to the unassigned computer.
        """
        self.ass_response = self.client.get(
            reverse('computer_detail', kwargs={'pk': 1}))

        self.unass_response = self.client.get(
            reverse('computer_detail', kwargs={'pk': 2}))

    def test_status_code(self):
        """This test asserts that the computer object is returned. The status code 200 means everything is fine."""
        self.assertEqual(self.ass_response.status_code, 200)
        self.assertEqual(self.unass_response.status_code, 200)

    def test_data_is_correct(self):
        """This test asserts that the text and bool fields from the computer object appear correctly in the returned data."""
        self.assertIn(self.assigned_Computer.make.encode(),
                      self.ass_response.content)
        self.assertIn(self.unassigned_Computer.make.encode(),
                      self.unass_response.content)
        self.assertIn(self.assigned_Computer.manufacturer.encode(),
                      self.ass_response.content)
        self.assertIn(self.unassigned_Computer.manufacturer.encode(),
                      self.unass_response.content)
        self.assertIn(self.assigned_Computer.has_been_assigned.encode(),
                      self.ass_response.content)
        self.assertIn(self.unassigned_Computer.has_been_assigned.encode(),
                      self.unass_response.content)

    def test_delete(self):
        """This test asserts that the assigned computer cannot be deleted and remains in the database but the unassigned computer is deleted"""

        self.delete_response_no_go = self.client.delete(
            reverse('computer_delete', kwargs={'pk': 1}))
        self.delete_response_yes_go = self.client.delete(
            reverse('computer_delete', kwargs={'pk': 2}))

        self.assertEqual(self.delete_response_no_go.status_code, 302)
        self.assertEqual(self.delete_response_yes_go.status_code, 302)
