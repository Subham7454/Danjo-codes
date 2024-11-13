from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVriety(models.Model):

    CHAI_TYPE_CHOICE=[
    ('ML','MASALA'),    
    ('GR','GINGER'),    
    ('KL','KIWI'),    
    ('PL','PALIN'),    
    ('EL','ELAICHI'),    
     ]    

    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_aded=models.DateTimeField(default=timezone.now())
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)