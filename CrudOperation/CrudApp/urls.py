
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'employee',EmployeeViewSet)

urlpatterns = [
    path('index',views.index,name='index'),
    path('add',views.Add,name='add'),
    path('edit',views.Edit,name='edit'),
    path('update',views.Update,name='update'),
    path('', include(router.urls)),
    path('test',views.ApiTest,name='test'),
    path('test_list',views.Test_list,name='test_list')
]
