from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
    def validation_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seats Filled')
        return value
    def validation(self,data):
        name=data.get('name')
        city=data.get('city')

        if city and name:
            if name.lower()=='fayaztunio' and city.lower()!='karachi':
                raise serializers.ValidationError('The City Must be Karachi')
            return data
        return print('City and Name are Required')
        