from django.urls import path, include
from contacts.apps import ContactsConfig
from contacts.views import contacts

app_name = ContactsConfig.name

urlpatterns = [
    path('contacts/', contacts, name="contacts"),
]