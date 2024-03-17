import uuid
from django.test import TestCase
from rest_framework.test import APIClient
#from rest_framework_simplejwt.tokens import RefreshToken
#from user.models import User
from data_api.models import my_models

class TestAttributeNameSetup(TestCase):

    def set_up(self):
        self.client = APIClient()
        fake_email = f"{str(uuid.uuid4())}@email.com"
        #self.user = User.objects.create(
        #    email=str(uuid.uuid4()),
        #)
        #refresh = RefreshToken.for_user(self.user)
        #self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')
        self.my_model = my_models['AttributeName'].objects.create(
            id = 1,
            nazev = "Barva",
            #user = self.user
        )
