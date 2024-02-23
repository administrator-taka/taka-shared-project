# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from myapp.model.models import User, Entry
from myapp.serializer.serializer import UserSerializer, EntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = ('author', 'status')
