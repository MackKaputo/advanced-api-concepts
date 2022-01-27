from rest_framework import serializers
from .models import User, Course

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "password"]
        # Do not return the password
        extra_kwargs ={
            "password": { "write_only": True}
        }

    def create(self, validated_data):
        #following is to hash the password
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    surname = serializers.CharField(max_length=200)
    age = serializers.IntegerField()

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    number_of_objectives = serializers.IntegerField()
    id = serializers.IntegerField()
    students = StudentSerializer(required=False, many=True)
    # class Meta:
    #     model = Course
    #     fields = ["id", "name", "description", "number_of_objectives"]