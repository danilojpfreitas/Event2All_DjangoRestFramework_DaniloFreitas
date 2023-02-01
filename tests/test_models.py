from django.test import TestCase
from event2all.models import User, Event, Quotation, Guest, ToDoList


class ModelTestCase(TestCase):

    def setUp(self):
        self.user = User(
            name="TestUni", email="testUni@testeUni.com", birth_date="0101-01-01", password="testUnitestUni"
        )
        self.event = Event(
            place="Maceio", name="Festa1", date="2021-01-01", managers="2", invite_number=2, event_budget=2
        )
        self.quotation = Quotation(
            description="Test1", contact="Test1", provider="Test1", expected_expense=2, actual_expense=100, amount_already_paid=100
        )
        self.guest = Guest(
            name="Danilo", contact="1234", isConfirmed="yes"
        )
        self.to_do_list = ToDoList(
            content="test1"
        )


    def test_verifica_atributos_do_user(self):
        """Teste que verifica os atributos do USER"""
        self.assertEquals(self.user.name, 'TestUni')
        self.assertEquals(self.user.email, 'testUni@testeUni.com')
        self.assertEquals(self.user.birth_date, '0101-01-01')
        self.assertEquals(self.user.password, 'testUnitestUni')

    def test_verifica_atributos_do_event(self):
        """Teste que verifica os atributos do Event"""
        self.assertEquals(self.event.place, 'Maceio')
        self.assertEquals(self.event.name, 'Festa1')
        self.assertEquals(self.event.date, '2021-01-01')
        self.assertEquals(self.event.managers, '2')
        self.assertEquals(self.event.invite_number, 2)
        self.assertEquals(self.event.event_budget, 2)

    def test_verifica_atributos_do_quotation(self):
        """Teste que verifica os atributos de Quotation"""
        self.assertEquals(self.quotation.description, "Test1")
        self.assertEquals(self.quotation.contact, "Test1")
        self.assertEquals(self.quotation.provider, "Test1")
        self.assertEquals(self.quotation.expected_expense, 2)
        self.assertEquals(self.quotation.actual_expense, 100)
        self.assertEquals(self.quotation.amount_already_paid, 100)

    def test_verifica_atributos_de_guest(self):
        """Teste que verifica os atributos de Guest"""
        self.assertEquals(self.guest.name, "Danilo")
        self.assertEquals(self.guest.contact, "1234")
        self.assertEquals(self.guest.invite, False)
        self.assertEquals(self.guest.isConfirmed, "yes")

    def test_verifica_atributos_de_todolist(self):
        """Teste que verifica os atributos de ToDoList"""
        self.assertEquals(self.to_do_list.content, "test1")
        self.assertEquals(self.to_do_list.done, False)





