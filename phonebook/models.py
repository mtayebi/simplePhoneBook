from django.db import models


# Create phone book model
class Contact(models.Model):
    """
    define phone book fields
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"