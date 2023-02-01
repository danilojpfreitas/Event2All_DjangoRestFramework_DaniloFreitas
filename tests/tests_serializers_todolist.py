from django.test import TestCase
from event2all.models import ToDoList
from event2all.serializer import ToDoListSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self) -> None:

        self.to_do_list = ToDoList(
            content="test1"
        )
        self.serializer = ToDoListSerializer(instance=self.to_do_list)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'content', 'done', 'created_at', 'updated_at', 'event_id']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['content'], self.to_do_list.content)
        self.assertEqual(data['done'], self.to_do_list.done)
        self.assertEqual(data['created_at'], self.to_do_list.created_at)
        self.assertEqual(data['updated_at'], self.to_do_list.updated_at)
