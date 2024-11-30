from faker import Faker
import random

class Course:
    def __init__(self, fake):
        self.city = "{}".format(fake.city())
        self.name = "{} {} {}".format(self.city,random.choice(["Creek",
                                                               "Cedar",
                                                               "Well",
                                                               "Mountain",
                                                               "Park",
                                                               "Hills",
                                                               "Plains",
                                                               "Springs",
                                                               "Forest",
                                                               "Arena",
                                                               "Sands",
                                                               "Dunes",
                                                               "Swamp",
                                                               "Lake",
                                                               "Outback",
                                                               "Marshlands"]), 
                                                random.choice(["Golf Club",
                                                               "Country Club",
                                                               "Members Club",
                                                               "Golf & Padel Club",
                                                               "G.C",
                                                               "C.C",
                                                               "Ridge",
                                                               "Inbread association",
                                                               "Gentlemens hangout",
                                                               "Waterpolo and Golf",
                                                               "Canasta and Golf"]))

def get_course_name(course):
    return "\t^^^^ {} - {} ^^^^".format(course.name.upper(), course.city.upper())