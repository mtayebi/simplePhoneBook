from django.urls import path
from .views import home, ContactList, ContactCreate, ContactUpdate, ContactDelete

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('contact/', ContactList.as_view(), name='contactlist'),
    path('newcontact/', ContactCreate.as_view(), name='newcontact'),
    path('updatecontact/<int:pk>', ContactUpdate.as_view(), name='updatecontact'),
    path('deletecontact/<int:pk>', ContactDelete.as_view(), name='deletecontact'),
]
