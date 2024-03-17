from rest_framework import status
from data_api.tests.test_setup import TestAttributeNameSetup

class TestAttributeNameLogAPIs(TestAttributeNameSetup):
    def test_get_all_attribute_name(self):
        response = self.client.get('/detail/AttributeName')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more integration tests for other endpoints and functionalities
