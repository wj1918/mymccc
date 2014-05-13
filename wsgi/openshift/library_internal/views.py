from django.shortcuts import render
from django.http import HttpResponse
from library_internal.models import CbDb
# Create your views here.

def index(request):
    return HttpResponse("Hello, You're at the library internal.")

def report(request, report_name):
    cbdb_list = CbDb.objects.all()[:100]
    context = {'cbdb_list': cbdb_list}
    return render(request, 'report/CB-Label.html', context)
