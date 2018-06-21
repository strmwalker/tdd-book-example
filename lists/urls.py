from django.urls import path

from lists.views import new_list, view_list

urlpatterns = [
    path('new', new_list, name='new_list'),
    path('<int:list_id>/', view_list, name='view_list')
]
