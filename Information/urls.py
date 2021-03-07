from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import UserDocumentsView, UserDocumentsDetailsview

urlpatterns = [
    url(r'^$', UserDocumentsView.as_view(), name='file-upload'),
    path('<int:id>/', UserDocumentsDetailsview.as_view(), name='taskdetailsview')
]
