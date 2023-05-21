from rest_framework import serializers
from .models import ListModel
#from utils import datasolve

class ChatSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListModel
        fields = '__all__'
        #exclude = ['is_delete']
        read_only_fields = ['id']
