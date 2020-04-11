from django.db import models

# Create your models here.
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
    student_batch = models.CharField(default= "NotGiven ",max_length=50)
    student_academic_year = models.CharField(default="NotGiven ",max_length=50)
    student_admission_category = models.CharField(default = " NotGiven",max_length=50)
    student_fee_category = models.CharField(default= " NotGiven",max_length=50)
    student_image = models.CharField(max_length=100)
    def __str__(self):
        return self.student_name

def upload_path(instance,filename):
    return '/'.join(['images',filename])

class Student_Image(models.Model):
    student_image = models.ImageField(upload_to=upload_path)