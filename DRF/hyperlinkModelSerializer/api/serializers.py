from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='students',
        lookup_field='slug'
     )
    students = serializers.HyperlinkedRelatedField(
        view_name='students',
        lookup_field='name',
        many=True,
        read_only=True
    )

    class Meta:
        model = Student
        fields = ['id','url','name','roll','city','students']