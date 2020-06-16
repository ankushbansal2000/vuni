from rest_framework import serializers
from .models import Student_Details,Student_Image


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student_Details
        # fields = ['id','student_name','student_DOB','student_father','student_mother','student_category','student_gender','student_nationality','student_domicile','student_blood'
        #             ,'student_email','student_parent_email','student_ph','student_father_ph','student_aadhar','student_corr_address1','student_corr_address2','student_corr_city','student_corr_district','student_corr_state','student_corr_country',
        #                 'student_corr_pincode','student_parr_address','student_parraddress','student_parrcity','student_parrdistrict','student_parrstate','student_parrcountry',
        #                 'student_parrpincode','student_course']
        fields = "__all__"
class StudentGet(serializers.ModelSerializer):
    class Meta:
        model = Student_Details
        fields = "__all__"

class StudentUpdate(serializers.ModelSerializer):
    class Meta:
        model = Student_Details
        fields = ['student_batch']

class StudentFeePay(serializers.ModelSerializer):
    class Meta:
        model = Student_Details
        fields = ['student_fee_deatils']

class StudentImage(serializers.ModelSerializer):
    class Meta:
        model = Student_Image
        fields = "__all__"