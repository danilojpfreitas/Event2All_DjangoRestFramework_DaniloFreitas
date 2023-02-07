import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from event2all.models import User, Event


def new_events(number_event):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(number_event):
        place = fake.address()
        name = fake.name()
        date = "{}-{}-{}".format(random.randrange(1900, 2023), random.randrange(10, 13), random.randrange(1, 31))
        managers = fake.name()
        invite_number = random.randrange(1, 1000)
        event_budget = random.randrange(1, 1000)
        user_id = random.randrange(1,50)
        p = Event(place=place, name=name, date=date, managers=managers, invite_number=invite_number, event_budget=event_budget, user_id=user_id)
        p.save()


new_events(50)
print("Sucesso Event!")