from rest_framework import serializers
from  .models import Student

# Validators
def start_with_r(value):
    if value[0].lower()!= 'r':
        raise serializers.ValidationError('Name should be start with R')
    
    
class StudentSerailizer(serializers.ModelSerializer):
    name= serializers.CharField(max_length=100, validators=[start_with_r])
    class Meta:
        model= Student
        fields= ['id','name','roll','city']
    
    
# Field level validation
    def validate_roll(self, value):
        print('value=',value)
        if value >= 200:
            raise serializers.ValidationError('Seat Full!!')
        return value

# Object level validation    
    def validate(self, data):
        print('data=',data)
        nm= data.get('name')
        ct= data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data
            