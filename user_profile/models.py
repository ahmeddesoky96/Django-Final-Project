from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class MyUser(models.Model):

    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=75,db_column='email',
        validators=[
            RegexValidator(
                r'[^@]+@[^@]+\.[^@]+',
                'Enter a valid email.'
            )
        ])
    password=models.CharField(max_length=20)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                r'^01[0125][0-9]{8}$',
                'Enter a valid Egyption phone number.'
            )
        ]
    )
    image = models.ImageField(null=True,upload_to="profile_images/")
    birth_date= models.DateField()
    facebook_profile= models.URLField()
    country= models.CharField()

    def __str__(self) -> str:
        return self.first_name+" "+self.last_name
