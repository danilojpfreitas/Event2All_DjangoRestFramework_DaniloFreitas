'''from rest_framework.test import APITestCase
from event2all.models import User, Event
from django.contrib.auth.models import User as Us
from django.urls import reverse
from rest_framework import status


class EventsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = Us.objects.create_superuser(
            email='asdf@gmail.com',
            password='hiwa_asdf',
            username='smile as we go ahead'
        )
        self.client.force_authenticate(self.user)

        self.list_url = reverse('User-list')

        self.user_1 = User.objects.create(
            name="Test1", email="test1@teste1.com", birth_date="0101-01-01", password="test1test1"
        )

        self.list_url = reverse('User-list')

        self.event_1 = Event.objects.create(
            place="test1", name="test1", date="0101-01-01", managers='10', invite_number=10, event_budget=10, user_id=1
        )
        self.event_2 = Event.objects.create(
            place="test2", name="test2", date="0202-02-02", managers='20', invite_number=20, event_budget=20, user_id=1
        )

    def test_requisicao_GET_para_listar_event(self):
        """Teste para verificar a requisição GET para listar os Event"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)'''