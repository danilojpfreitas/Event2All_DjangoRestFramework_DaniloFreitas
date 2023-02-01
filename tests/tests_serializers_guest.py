from django.test import TestCase
from event2all.models import Guest
from event2all.serializer import GuestSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self) -> None:

        self.guest = Guest(
            name="Danilo", contact="1234", isConfirmed="yes"
        )
        self.serializer = GuestSerializer(instance=self.guest)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'contact', 'invite', 'isConfirmed', 'created_at', 'updated_at', 'event_id']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['name'], self.guest.name)
        self.assertEqual(data['contact'], self.guest.contact)
        self.assertEqual(data['invite'], self.guest.invite)
        self.assertEqual(data['isConfirmed'], self.guest.isConfirmed)
        self.assertEqual(data['created_at'], self.guest.created_at)
        self.assertEqual(data['updated_at'], self.guest.updated_at)
