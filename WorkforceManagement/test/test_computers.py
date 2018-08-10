class Computer_Test(TestCase):
    """Tests computer functionality for WorkforceManagement
    Author: Erin Meaker
    """

    def test_computer_setup(self):
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

        """ass_response refers to the object returned when pulling an "assigned computer" from the data above. It is not a fart.
        Likewise, "unass_response" refers to the unassigned computer.
        """
        ass_response = self.client.get(
            reverse('computer_detail', kwargs={'pk': 1}))

        unass_response = self.client.get(
            reverse('computer_detail', kwargs={'pk': 2}))

    def test_status_code(self):
        """This test asserts that the computer object is returned. The status code 200 means everything is fine."""
        self.assertEqual(ass_response.status_code, 200)
        self.assertEqual(unass_response.status_code, 200)

    def test_data_is_correct(self):
        """This test asserts that the text and bool fields from the computer object is appearing correctly in the returned data."""
        self.assertIn(assigned_Computer.make.encode(),
                      ass_response.content)
        self.assertIn(unassigned_Computer.make.encode(),
                      unass_response.content)
        self.assertIn(assigned_Computer.manufacturer.encode(),
                      ass_response.content)
        self.assertIn(unassigned_Computer.manufacturer.encode(),
                      unass_response.content)
        self.assertIn(assigned_Computer.has_been_assigned.encode(),
                      ass_response.content)
        self.assertIn(unassigned_Computer.has_been_assigned.encode(),
                      unass_response.content)

    def test_delete(self):
        """This test asserts that the assigned computer cannot be deleted and remains in the database but the unassigned computer is deleted"""
