from rest_framework import serializers
from .models import ListModel
#from utils import datasolve

class NoteSerializers(serializers.ModelSerializer):
    note_desc = serializers.SerializerMethodField()

    def get_note_desc(self, obj):
        return obj.note[:200]

    class Meta:
        model = ListModel
        fields = ['note_code','note_title','note_tags','rating','creater','update_time','create_time','note_desc']
        #exclude = ['is_delete','note']
        read_only_fields = ['id']
