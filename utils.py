import os


def read_requirements():
    req_path = os.path.join(os.getcwd()+ '/requirements.txt')
    print(req_path)
    with open(req_path) as file:
        return file.read()



from faker import Faker

fake = Faker()
for i in range(100):
    fake.name()