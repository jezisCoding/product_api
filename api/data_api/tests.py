from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from copy import deepcopy

# Create your tests here.

class TestModelNameIdView(APITestCase):

    def test_one_AttributeName_import(self):
        ind = {"AttributeName": {"id": 1, "nazev": "Barva"}}
        response = self.client.post(reverse("data_import"),
                ind, format="json")
 
        exd = deepcopy(ind)
        exd["AttributeName"].update({"kod": "", "zobrazit": True})
        exd = [exd]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, exd)
