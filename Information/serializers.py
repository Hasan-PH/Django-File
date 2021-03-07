from rest_framework import serializers
from .models import UserDocuments
from django.core.files.storage import FileSystemStorage
import datetime
from django.utils.timezone import utc
from datetime import datetime
import os


class UserDocumentsSerializer(serializers.ModelSerializer):
    class Meta():
        fields = '__all__'
        model = UserDocuments

    def create(self, validated_data):
        doc = validated_data.get('doc')
        ud = UserDocuments()
        ud.doc = doc
        ud.save()
        ud.doc_name = str(ud.doc)
        if str(ud.doc).find('.') != -1:
            ud.doc_type = str(ud.doc).split(".")[-1]
        else:
            ud.doc_type = ''
        ud.doc_link = '/media/' + str(ud.doc)
        ud.save()

        return ud
        # return UserDocuments.objects.create(doc_name='debugging', doc=doc)

    def update(self, instance, validated_data):
        print(" I am here!!!!!!!!!!")
        # obj = UserDocuments.objects.filter(id=validated_data.get('id'))
        print(validated_data.get('doc'))
        os.remove('cd ../..' + instance.doc_link)
        instance.doc = validated_data.get('doc')
        instance.save()
        return instance