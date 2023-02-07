from faker import Faker

fake = Faker() #instanciamos

data= [] #creamos una lista vacía

for _ in range(5000):#en cada lista se esta agg una tupla de 7 elementos
    data.append((fake.uuid4(),fake.name(), fake.company(), fake.job(),
                fake.email(), fake.phone_number(), fake.mac_address()))