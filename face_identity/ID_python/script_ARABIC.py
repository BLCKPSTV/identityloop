from faker import Faker
fake = Faker('ar_PS')

for i in range(100):

        print(" " + "{" "\n"
        "      " + '"name"' + " " + ":" + " " + '"{}"'.format(fake.name()) + "," "\n"
        "      " + '"country"' + " " + ":" + " " + '"{}"'.format(fake.country()) + "," "\n"
        "      " + '"city"' + " " + ":" + " " + '"{}"'.format(fake.city()) + "," "\n"
        "      " + '"postcode"'  + " " + ":" + " " + '"{}"'.format(fake.postcode()) + "," "\n"
        "      " + '"lat"' + " " + ":" + " " + '"{}"'.format(fake.latitude()) + "," "\n"
        "      " + '"long"' + " " ":" + " " + '"{}"'.format(fake.longitude()) + "," "\n"
        "      " + '"zip code"' + " " + ":" + " " + '"{}"'.format(fake.zipcode()) + "," "\n"
        "      " + '"street name"' + " " + ":" + " " + '"{}"'.format(fake.street_name()) + "," "\n"
        "      " + '"license plate"' + " " + ":" + " " + '"{}"'.format(fake.license_plate()) + "," "\n"
        "      " + '"phone number"' + " " + ":" + " " + '"{}"'.format(fake.phone_number()) + "," "\n"
        "      " + '"ipv4"' + " " + ":" + " " + '"{}"'.format(fake.ipv4(network=False)) + "," "\n"
        "      " + '"email"' + " " + ":" + " " + '"given randomEmail"' + "," "\n"
        "      " + '"username"' + " " + ":" + " " + '"{}"'.format(fake.user_name()) + "," "\n"
        "      " + '"password"' + " " + ":" + " " + '"{}"'.format(fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)) + "," "\n"
        "      " + '"iban"' + " " + ":" + " " + '"{}"'.format(fake.iban()) + "," "\n"
        "      " + '"credit card"' + " " + ":" + " " + '"{}"'.format(fake.credit_card_number()) + "," "\n"
        "      " + '"credit card security code"' + " " + ":" + " " + '"{}"'.format(fake.credit_card_security_code()) + "," "\n"
        "      " + '"cryptocurrency code"' + " " + ":" + " " + '"{}"'.format(fake.cryptocurrency_code()) + "," "\n"
        "      " + '"profession"' + " " + ":" + " " + '"{}"'.format(fake.job()) + "\n"
        "     " + "},")
