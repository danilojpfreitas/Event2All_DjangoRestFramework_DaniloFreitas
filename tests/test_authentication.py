from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.list_url = reverse('User-list')
        self.user = User.objects.create_user('danilo', password='123456')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autentição de um user com as credenciais corretas"""
        user = authenticate(username='danilo', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica uma requisição GET sem autenticar"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_de_user_com_username_incorreto(self):
        """Teste que verifica a autenticação de um user com o Username incorreto"""
        user = authenticate(username='anadelia', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_de_user_com_password_incorreto(self):
        """Teste que verifica a autenticação de um user com o Password incorreto"""
        user = authenticate(username='danilo', password='654321')
        self.assertFalse((user is not None) and user.is_authenticated)


"""    def test_requisicao_get_com_user_autenticado(self):
        Teste que verifica uma requisição GET com o user autenticado
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)"""
