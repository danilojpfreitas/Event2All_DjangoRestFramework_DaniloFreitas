from django.test import TestCase
from event2all.models import User
from seeds import new_users


class SeedsDataTestCase(TestCase):

    seeds = [new_users(50)]

    def test_verifica_carregamento_dos_seeds(self):
        todos_os_user = User.objects.all()
        self.assertEqual(len(todos_os_user), 50)