import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from event2all.models import User, Event


def new_users(number_users):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(number_users):
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        birth_date = "{}-{}-{}".format(random.randrange(1900, 2023), random.randrange(10, 13), random.randrange(1, 31))
        password = "{}".format(random.randrange(10000000, 99999999))
        p = User(name=name, email=email, birth_date=birth_date, password=password)
        p.save()


new_users(50)
print("Sucesso User!")

