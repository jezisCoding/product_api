#import uuid
from django.test import TestCase
from rest_framework.test import APIClient
#from rest_framework_simplejwt.tokens import RefreshToken
#from user.models import User
from data_api.models import my_models

class TestAttributeNameSetup(TestCase):

    def set_up(self):
        self.client = APIClient()
        #fake_email = f"{str(uuid.uuid4())}@email.com"
        #self.user = User.objects.create(
        #    email=str(uuid.uuid4()),
        #)
        #refresh = RefreshToken.for_user(self.user)
        #self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')
        self.my_model = my_models['AttributeName'].objects.create(
            id = 1,
            nazev = "Barva"
            #user = self.user
        )

class TestAttributeValueSetup(TestCase):

    def set_up(self):
        self.client = APIClient()
        self.my_model = my_models['AttributeValue'].objects.create(
            id = 1,
            hodnota = 'modrá'
        )

class TestAttributeSetup(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.my_model = my_models['Attribute'].objects.create(
            id = 1,
            nazev_atributu = 1,
            hodnota_atributu = 1
        )

class TestProductSetup(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.my_model = my_models['Product'].objects.create(
            id = 1,
            nazev = "Whirlpool B TNF 5323 OX",
            description = "Volně stojící kombinovaná lednička se šestým "
                + "smyslem. Díky tomuto šestému smyslu FreshLock dokáže "
                + "obnovit teplotu 5× rychleji",
            cena = 21566,
            mena = "CZK",
            published_on = null,
            is_published = False
        )

class TestProductAttributesSetup(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.my_model = my_models['ProductAttributes'].objects.create(
            id = 1,
            attribute = 19,
            product = 1
        )

class TestImageSetup(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.my_model = my_models['Image'].objects.create(
            id = 1,
            obrazek = "https://free-images.com/or/4929/fridge_t_png.jpg"
        )

class TestProductImageSetup(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.my_model = my_models['ProductImage'].objects.create(
            id = 1,
            product = 1,
            obrazek = 1,
            nazev = "hlavní foto"
        )

class TestCatalogSetup(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.my_model = my_models['Catalog'].objects.create(
            id = 1,
            nazev = "Výprodej 2018",
            obrazek = 4,
            products = [1, 2, 3, 4, 5],
            attributes = [2, 4, 21, 24]
        )
