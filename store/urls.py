from django.urls import path
from . import views
app_name='store'
urlpatterns=[
    path('',views.home, name='home'),
    path('<slug:slug>/',views.details,name='details'),
    path('category/<slug:category_slug>/', views.category, name='category'),
]