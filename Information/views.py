# from django.shortcuts import render
# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# from .models import UserDocuments
# import pathlib

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDocumentsSerializer
from .models import UserDocuments
from rest_framework import generics, mixins


# def upload(request):
#     return render(request, 'upload.html', {})
#


# def upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#
#         ud = UserDocuments()
#         ud.doc_name = filename
#         ud.doc_link = uploaded_file_url
#         ud.doc_type = 'pdf'
#         ud.save()
#
#         return render(request, 'upload.html', {'uploaded_file_url': uploaded_file_url})
#     return render(request, 'upload.html', {})


# class UserDocumentsView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#
#     def get(self, request, *args, **kwargs):
#         docs = UserDocuments.objects.all()
#         serializer = UserDocumentsSerializer(docs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         file_serializer = UserDocumentsSerializer(data=request.data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDocumentsView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = UserDocumentsSerializer
    queryset = UserDocuments.objects.all().order_by("created_at")

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class UserDocumentsDetailsview(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = UserDocumentsSerializer
    queryset = UserDocuments.objects.all().order_by("created_at")
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request, id)