from rest_framework import serializers
from .models import Student




class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['name','roll']
        extra_kwargs = {'roll':{'read_only':True}}



        # ---------->>>>>>>>>>>>Validationss- OF - RestAPI---------

            # field -level-validation field
    def validate_roll(self, value):
        if value > 10:
            raise serializers.ValidationError('Name must be less than 10 characters')
        return value
            # Oject level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'moor' and ct.lower() != 'lhr':
            raise serializers.ValidationError({'name':'City must be Lhr'})
        return data


                 # validators


# class StudentSerializer(serializers.ModelSerializer):
#     def start_with_r(value):
#         if not value[0].lower() != 'r':
#             raise serializers.ValidationError('Name must start with r')
#         return value
#     name = serializers.CharField(validators=[start_with_r])
#     class Meta:
#         model = Student
#         fields = '__all__'
#         extra_kwargs = {'roll':{'read_only':True}}
