from django import forms
from multiselectfield import MultiSelectFormField

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

GENDER_CHOICES = (
    ('Male','MALE'),
    ('Female','FEMALE'),
)



class EnquiryForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )

    email = forms.EmailField(
        label="Enter Your Email ID",
        widget = forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )

    mobile = forms.IntegerField(
        label="Enter Your Mobile Number",
        widget = forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
            }
        )
    )

    cources = MultiSelectFormField(choices=COURSE_CHOICES,
                                    label="Select your cource")

    trainer = MultiSelectFormField(choices=TRAINER_CHOICE,
                                    label="Select your trainer")

    shift = MultiSelectFormField(choices=SHIFT_CHOICES,
                                    label="Select your shift")

    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=GENDER_CHOICES,
        label="Select your Gender"
    )

    

# from .models import EnquiryData

# class EnquiryForm(forms.ModelForm):
#     class Meta:
#         model = EnquiryData
#         fields = "__all__"