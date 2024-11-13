from django.shortcuts import render
from .models import ChaiVriety
from django.shortcuts import get_object_or_404

# Create your views here.

def all_chai(request):
    chais = ChaiVriety.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})

def chai_deatail(request,chai_id):
    chai=get_object_or_404(ChaiVriety,pk=chai_id)
    return render(request,'chai/chai_details.html',{'chai':chai})