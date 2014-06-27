from django.shortcuts import render
from django.http import HttpResponse
from library_internal.models import CbDb
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from library_internal.serializers import UserSerializer, GroupSerializer
# Create your views here.

def index(request):
    return HttpResponse("Hello, You're at the library internal.")

def report(request, report_name):
    cbdb_list = CbDb.objects.all()[:100]
    context = {'cbdb_list': cbdb_list}
    return render(request, 'report/CB-Label.html', context)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
