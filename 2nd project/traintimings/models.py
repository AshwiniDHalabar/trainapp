from django.db import models

# Create  your  models here.
class train(models.Model):
    train_id = models.IntegerField()
    name = models.CharField(max_length=50)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    duration = models.CharField(max_length=50)
    class Meta:
        db_table = "train"
