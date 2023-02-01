from django.test import TestCase
from event2all.models import Quotation
from event2all.serializer import QuotationSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self) -> None:

        self.quotation = Quotation(
            description="Test1", contact="Test1", provider="Test1", expected_expense=2, actual_expense=100, amount_already_paid=100
        )
        self.serializer = QuotationSerializer(instance=self.quotation)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'description', 'contact', 'provider', 'expected_expense', 'actual_expense', 'amount_already_paid', 'created_at', 'updated_at', 'event_id']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['description'], self.quotation.description)
        self.assertEqual(data['contact'], self.quotation.contact)
        self.assertEqual(data['provider'], self.quotation.provider)
        self.assertEqual(data['expected_expense'], self.quotation.expected_expense)
        self.assertEqual(data['actual_expense'], self.quotation.actual_expense)
        self.assertEqual(data['amount_already_paid'], self.quotation.amount_already_paid)
        self.assertEqual(data['created_at'], self.quotation.created_at)
        self.assertEqual(data['updated_at'], self.quotation.updated_at)
