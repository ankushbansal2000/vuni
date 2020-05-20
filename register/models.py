from django.db import models
from jsonfield import JSONField
from djongo.models import ArrayField

# Create your models here.
class fee_details(models.Model):
    amount_payable=models.IntegerField(blank=True)
    payment_mode=models.CharField(max_length=50,blank=True)
    cheque_no = models.CharField(blank=True,max_length=50)


class Student_Details(models.Model):
    student_admission_status = models.CharField(default = "pending",max_length=50)
    student_name=models.CharField(max_length=50)
    student_DOB=models.DateField()
    student_father=models.CharField(max_length=50)
    student_mother=models.CharField(max_length=50)
    student_category=models.CharField(max_length=10)
    student_gender=models.CharField(max_length=20)
    student_nationality=models.CharField(max_length=20)
    student_domicile=models.CharField(max_length=50)
    student_blood=models.CharField(max_length=5)
    student_email=models.EmailField()
    student_parent_email=models.EmailField()
    student_ph=models.BigIntegerField()
    student_father_ph=models.BigIntegerField()
    student_aadhar=models.BigIntegerField()
    student_corr_address1=models.CharField(max_length=300)
    student_corr_address2=models.CharField(max_length=300)
    student_corr_city=models.CharField(max_length=50)
    student_corr_district=models.CharField(max_length=50)
    student_corr_state=models.CharField(max_length=50)
    student_corr_country=models.CharField(max_length=50)
    student_corr_pincode=models.IntegerField()
    student_parr_address=models.CharField(max_length=300)
    student_parraddress=models.CharField(max_length=300)
    student_parrcity=models.CharField(max_length=50)
    student_parrdistrict=models.CharField(max_length=50)
    student_parrstate=models.CharField(max_length=50)
    student_parrcountry=models.CharField(max_length=50)
    student_parrpincode=models.IntegerField()
    student_course=models.CharField(max_length=50)
    student_batch = models.CharField(max_length=50, blank = True)
    student_fee_pattern = models.CharField(max_length=50, blank = True)
    student_image = models.CharField(max_length=100)
    student_fee_deatils = JSONField(null=True)

    def __str__(self):
        return self.student_name

def upload_path(instance,filename):
    return '/'.join(['images',filename])

class Student_Image(models.Model):
    student_image = models.ImageField(upload_to=upload_path)


