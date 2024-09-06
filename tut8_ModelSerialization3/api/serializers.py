from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)
    class Meta:
        model=Student
        fields=['name','roll','city']
        # read_only_fields=['name','roll']
        # extra_kwargs={'name':{'read_only':True}}
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')

        # Ensure name and city are not None or empty
        if not name:
            raise serializers.ValidationError({'name': 'Name field is required.'})
        if not city:
            raise serializers.ValidationError({'city': 'City field is required.'})

        # Additional logic for name and city validation
        if name.lower() == 'fayaz' and city.lower() != 'larkana':
            raise serializers.ValidationError('The City Must be Larkana.')

        return data
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seats Are Full')
        return value