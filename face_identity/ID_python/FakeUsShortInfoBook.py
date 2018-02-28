from faker import Faker
fake = Faker('it_IT')
it_it_fake = Faker('it_IT')

for i in range(100):

        print(" " + "{" "\n"
        "      " + '"male name"' + " " + ":" + " " + '"{}"'.format(fake.name_male()) + "," "\n"
        "      " + '"female name"' + " " + ":" + " " + '"{}"'.format(fake.name_female()) + "," "\n"
        "      " + '"country"' + " " + ":" + " " + '"{}"'.format(fake.country(it_IT)) + "," "\n"
        "      " + '"city"' + " " + ":" + " " + '"{}"'.format(fake.city()) + "," "\n"
        "      " + '"ipv4"' + " " + ":" + " " + '"{}"'.format(fake.ipv4(network=False)) + "," "\n"
        "      " + '"email"' + " " + ":" + " " + '"{}"'.format(fake.ascii_free_email()) + "," "\n"
        "      " + '"profession"' + " " + ":" + " " + '"{}"'.format(fake.job()) + "\n"
        "     " + "},")
