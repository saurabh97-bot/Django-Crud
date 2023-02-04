from django.shortcuts import render, redirect
from rest_framework.response import Response

from .models import Employee
from rest_framework import viewsets
from .serializers import EmployeeSerializer


# Create your views here.

def index(request):
    data = Employee.objects.all()
    return render(request, 'home.html', {'data': data})


def Add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('index')


def Edit(request):
    emp = Employee.objects.all()

    return redirect(request, 'index.html', {'emp': emp})


def Update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()

    return redirect(request, 'index.html')


# ViewSets define the view behavior.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# ========================================================

# Create API without drf

from django.core.serializers import serialize
from .models import Student
from django.http import HttpResponse


def ApiTest(request):
    q = Student.objects.all()
    data = serialize("json", q)
    return HttpResponse(data, content_type='application/json')


# =====================================================================
# API using Fuction Based View

from rest_framework.decorators import api_view
from .serializers import TestSerializer
from .models import TestModel
from django.http import JsonResponse


@api_view(['GET','POST'])
def Test_list(request):
    if request.method == 'GET':
        test = TestModel.objects.all()
        serializers = TestSerializer(test, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = TestSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=200)
        return Response(serializers.data, status=400)
