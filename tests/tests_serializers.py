from django.test import TestCase
from event2all.models import User
from event2all.serializer import UserSerializer

class ProgramaSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User(
            name="TestUni", email="testUni@testeUni.com", birth_date="0101-01-01", password="testUnitestUni"
        )
        self.serializer = UserSerializer(instance=self.user)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'email', 'birth_date', 'created_at', 'updated_at']))
