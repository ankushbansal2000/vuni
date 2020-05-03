from django.db import models

# Create your models here.
class FeePattern(models.Model):
    fee_pattern_class_name = models.CharField(max_length=50,default="not given")
    fee_pattern_type = models.CharField(default= "not given",max_length=50)
    fee_pattern_batch = models.CharField(default = "not given" ,max_length=50)

    def __str__(self):
        return self.fee_pattern_class_name  


class FeePatternHead(models.Model):
    fee_pattern_name = models.CharField(max_length=50)
    fee_collect_pattern = models.CharField(max_length=50)
    total_academic_fee = models.CharField(max_length=50)
    total_tution_fee = models.CharField(max_length=50)
    total_hostel_fee = models.CharField(max_length=50)


    def __str__(self):
        return self.fee_pattern_name