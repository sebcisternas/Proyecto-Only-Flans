from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Flan(models.Model):
   flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False,unique=-True)
   name = models.CharField(max_length=50)
   descripcion = models.TextField()
   image_url = models.URLField()
   slug = models.SlugField(unique=True,blank=True)
   is_private = models.BooleanField(default=False)
   price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Establecer un valor predeterminado de 0.00

   def save(self,*args,**kwargs):
        if not self.slug:
           self.slug = slugify(self.name)
        print("Llamando al método save() de la superclase...")
        super(Flan, self).save(*args, **kwargs)
        print("Objeto Flan guardado exitosamente.")
        
   def __str__(self):
       return self.name
   
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False,unique=-True)
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
       return self.customer_name
    
