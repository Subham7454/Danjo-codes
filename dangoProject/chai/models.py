from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChaiVriety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),    
        ('GR', 'GINGER'),    
        ('KL', 'KIWI'),    
        ('PL', 'PLAIN'),    
        ('EL', 'ELAICHI'),    
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)  # Corrected field name
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVriety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.user.username} review for {self.chai.name}'

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    chai_varieties = models.ManyToManyField(ChaiVriety, related_name='stores')  # Corrected spelling

    def __str__(self):
        return self.name

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVriety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'  # Corrected usage of 'chai.name'
