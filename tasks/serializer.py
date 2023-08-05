from rest_framework import serializers
from .models import Task


# creates python objects to JSON
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields= ('id', 'title', 'textfield', 'done')
        fields = '__all__'
