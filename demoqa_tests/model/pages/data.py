from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    male: str
    number: str
    day: str
    month: str
    year: str
    assert_data: str
    subject: str
    hobbies: str
    picture: str
    assert_picture: str
    address: str
    city: str
    state: str

user= User(
    first_name="John",
    last_name="Doe",
    email="john@doe.com",
    male="Male",
    number='1234567890',
    day=21,
    month='May',
    year='1999',
    assert_data='21 May,1999',
    subject='Maths',
    hobbies="Music",
    picture='resources/image.PNG',
    assert_picture='image.PNG',
    address='street',
    city='Delhi',
    state='NCR'
)

