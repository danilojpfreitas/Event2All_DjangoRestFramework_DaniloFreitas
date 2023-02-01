from django.test import TestCase
from event2all.models import Event
from event2all.serializer import EventSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self) -> None:

        self.event = Event(
            place="Maceio", name="Festa1", date="2021-01-01", managers="2", invite_number=2, event_budget=2
        )
        self.serializer = EventSerializer(instance=self.event)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'place', 'name', 'date', 'managers', 'invite_number', 'event_budget', 'created_at', 'updated_at', 'user_id']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['place'], self.event.place)
        self.assertEqual(data['name'], self.event.name)
        self.assertEqual(data['date'], self.event.date)
        self.assertEqual(data['managers'], self.event.managers)
        self.assertEqual(data['invite_number'], self.event.invite_number)
        self.assertEqual(data['event_budget'], self.event.event_budget)
        self.assertEqual(data['created_at'], self.event.created_at)
        self.assertEqual(data['updated_at'], self.event.updated_at)
