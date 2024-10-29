#from user.models import TabEmployee
from data_api.models import my_models 
from data_api.tests.test_setup import TestAttributeNameSetup
#import uuid

class TestAttributeNameModel(TestAttributeNameSetup):

    def test_attribute_name_str(self):
        self.set_up()
        self.assertEqual(str(self.my_model), "AttributeName 1 Barva")

    #def test_attribute_name_

    # Add more unit tests for various attributes and relationships
