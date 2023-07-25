from django.urls import path

from .views import index, v_add, v_list

urlpatterns = [path('', index), 
              path('vehiculo/add', v_add),
              path('vehiculo/list', v_list)]


