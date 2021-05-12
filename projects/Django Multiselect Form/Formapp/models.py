from django.db import models
from multiselectfield import MultiSelectField


COURSE_CHOICES = (
    ('python', 'PYTHON'),
    ('django', 'Django'),
    ('java', 'JAVA'),
    ('node', 'NodeJs'),
    ('sql', 'SQL'),
    ('flutter', 'Flutter'),
    ('react', 'ReactJS'),
)

TRAINER_CHOICE = (
    ('manas', 'Manas'),
    ('james', 'JAMES'),
    ('nara', 'Narayana'),
    ('malika', 'Mallika'),
    ('priti', 'Prithi'),
    ('Soma', 'Somasekhar'),
    ('Pr', 'Pratyusha'),
)

SHIFT_CHOICES = (
    ('morning','MORNING'),
    ('evening','EVENING'),
    ('noon','NOON'),
)

LOCATION_CHOICES = (
    ('HYD','HYDERABAD'),
    ('CHE','CHENNAI'),
    ('BANG','BANGALORE'),
)

class EnquiryData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    cources = MultiSelectField(max_length=200, choices=COURSE_CHOICES)
    trainer = MultiSelectField(max_length=100, choices=TRAINER_CHOICE)
    shift = MultiSelectField(max_length=100, choices=SHIFT_CHOICES)
    location = MultiSelectField(max_length=100, choices=LOCATION_CHOICES)
    gender = models.CharField(max_length=100)


