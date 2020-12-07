from django.db import models

class CustomerApp(models.Model):
    name = models.CharField(max_length=20)
    token = models.CharField(unique=True, max_length=10)
    paid_status = models.BooleanField()

    def __str__(self):
        return self.name + " | " + f"{self.id}"
