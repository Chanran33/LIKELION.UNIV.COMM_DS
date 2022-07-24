from django.shortcuts import render
from .models import Account

# Create your views here.
def test(request):
    readmes = Account.objects.all()
    return render(request, 'test.html',{'readmes' : readmes})
