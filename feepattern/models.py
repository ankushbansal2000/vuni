from django.db import models

# Create your models here.
class FeePattern(models.Model):
    fee_pattern_class_name = models.CharField(max_length=50,default=" ")
    fee_pattern_type = models.CharField(default= "",max_length=50)
    fee_pattern_tution_fee = models.IntegerField(default="0")
    fee_pattern_academic_fee = models.IntegerField(default="0")

    def __str__(self):
        return self.fee_pattern_class_name  