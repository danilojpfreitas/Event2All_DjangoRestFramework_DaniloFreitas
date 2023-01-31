from django.test import TestCase
from event2all.models import User


class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = User(
            name="TestUni", email="testUni@testeUni.com", birth_date="0101-01-01", password="testUnitestUni"
        )

    def test_verifica_atributos_do_user(self):
        """Teste que verifica os atributos do USER com valores default"""
        self.assertEquals(self.user.name, 'TestUni')
        self.assertEquals(self.user.email, 'testUni@testeUni.com')
        self.assertEquals(self.user.birth_date, '0101-01-01')
        self.assertEquals(self.user.password, 'testUnitestUni')
