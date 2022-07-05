from django.urls import path
from . import views
app_name='basket'
urlpatterns=[
    path('',views.summary,name='summary'),
    path('add/',views.addbasket,name='addbasket'),
    path('delete/',views.deletebasket,name='deletebasket'),
    path('update/',views.updatebasket,name='updatebasket'),
]