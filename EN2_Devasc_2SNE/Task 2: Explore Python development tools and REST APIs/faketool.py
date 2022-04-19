#!/usr/bin/env python3
from faker import Faker

fake = Faker()

print('My name is {} '.format(fake.name()) + 'and i wrote "{}'.format(fake.catch_phrase())+'" (ISBN {}).'.format(fake.isbn13()))


