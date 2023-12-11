from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.


class shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_video = models.FileField(upload_to='shops_photo/', blank=True)
    shop = models.CharField(max_length=255)
    shop_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'shop'
        ordering = ['-shop_date']

    def __str__(self):
        return f"{self.user}"
