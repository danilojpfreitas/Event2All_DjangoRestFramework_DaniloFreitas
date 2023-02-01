from rest_framework.test import APITestCase
from event2all.models import User
from django.contrib.auth.models import User as Us
from django.urls import reverse
from rest_framework import status


class UsersTestCase(APITestCase):

    def setUp(self):
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
        self.user_2 = User.objects.create(
            name="Test2", email="test2@teste2.com", birth_date="0202-02-02", password="test2test2"
        )

    def test_requisicao_GET_para_listar_user(self):
        """Teste para verificar a requisição GET para listar os User"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_POST_para_criar_user(self):
        """Teste para verificar a requisição POST para criar um User"""
        data = {
            'name': 'Test3',
            'email': 'test3@test3.com',
            'birth_date': '0303-03-03',
            'password': 'test3test3'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_DELETE_para_deletar_user(self):
        """Teste para verificar a requisição DELETE no USER"""
        response = self.client.delete('/user/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_PUT_para_atualizar_user(self):
        """Teste para verificar requisião PUT para atualizar USER"""
        data = {
            'name': 'Test4',
            'email': 'test4@test3.com',
            'birth_date': '0404-04-04',
            'password': 'test4test4'
        }
        response = self.client.put('/user/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

#    def test_fail(self):
#        self.fail('Teste falhou de propósito')
