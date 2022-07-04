from io import StringIO

import os
import django
import random
import tempfile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ElasticSearch.settings")
django.setup()

from faker import Faker

from home.models import ElasticSearchDemo


def create_data(n):
    fake = Faker("pt-BR")
    Faker.seed(10)
    for _ in range(n):
        title = fake.name()
        content = "{}@{}".format(title.lower(), fake.free_email_domain())
        content = content.replace(" ", "")
        p = ElasticSearchDemo(title=title, content=content)
        p.save()


create_data(80)
print("Created Fake Data!")
