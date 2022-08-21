from django.urls import path
from . import views
# app_name='foods'


urlpatterns = [
    path("",views.food_list,name='food_list'),
    path("<int:pk>/",views.food_details,name='details')
]


