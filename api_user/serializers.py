from api_user.models import Student, Hobi, Major
from rest_framework import serializers


class majorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ('name','id')

class StudentSerializer(serializers.ModelSerializer):
    hobies = serializers.StringRelatedField(many=True)
    major = majorSerializer(many=True,)

    class Meta:
        model = Student
        fields = ('id', 'name', 'lname', 'major', 'hobies')

class HobiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobi
        fields = ( 'hobi_name')