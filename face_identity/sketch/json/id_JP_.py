from faker import Faker
fake = Faker('ja_JP')


print('"name"' + " " + ":" + " " + '"{}"'.format(fake.romanized_name()))
print('"country"' + " " + ":" + " " + '"{}"'.format(fake.country()))
print('"city"' + " " + ":" + " " + '"{}"'.format(fake.city()))
