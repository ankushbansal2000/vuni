from rest_framework import serializers
from .models import Student_Details


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student_Details
        fields = ['id','student_name','student_DOB','student_father','student_mother','student_category','student_gender','student_nationality','student_domicile','student_blood'
                    ,'student_email','student_parent_email','student_ph','student_father_ph','student_aadhar','student_corr_address1','student_corr_address2','student_corr_city','student_corr_district','student_corr_state','student_corr_country',
                        'student_corr_pincode','student_parr_address','student_parraddress','student_parrcity','student_parrdistrict','student_parrstate','student_parrcountry',
                        'student_parrpincode','student_course']

class StudentGet(serializers.ModelSerializer):
    class Meta:
        model = Student_Details
        fields = "__all__"

class StudentUpdate(serializers.ModelSerializer):
    class Meta:
        model = Student_Details
        fields = ['student_admission_status','student_batch','student_academic_year','student_admission_category','student_fee_category']