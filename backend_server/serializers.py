from rest_framework import serializers
from .models import Users
from .models import acc_details
from .models import messages
from .models import warehouse

# Serializer for the Users model to convert Python objects to JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users  # Specifies the model to be serialized
        fields = ['id', 'username', 'password']  # Specifies the fields to include in the serialized representation
  
class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = warehouse  # Specifies the model to be serialized
        fields = ['email', 'username', 'password'] 

class AccDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = acc_details
        fields = ['email','username','name', 'surname', 'dob', 'phone_number','image'] 

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = messages
        fields = ['thread_number','email','subject','topic', 'message_body', 'timestamp_sent', 'timestamp_read','is_read', 'status','actions'] 


