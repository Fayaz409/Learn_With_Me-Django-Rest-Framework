from rest_framework import serializers
from .models import Student

def start_with_r(value):
    if value[0].lower() !='r':
        raise serializers.ValidationError('The name should start with R')


class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def validate(self,data):
        name=data.get('name')
        city=data.get('city')
        if name.lower()=='ravi' and city.lower()!='ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data

    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seats Full')
        return value


    def create(self,validated_data):    
        return Student.objects.create(**validated_data)
    def update (self,instance,validated_data):  #instance is the old data and validated_data is the new data                
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city==validated_data.get('city',instance.city)
        instance.save()
        return instance
