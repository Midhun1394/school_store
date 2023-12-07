from . import views
from django.urls import path,include

urlpatterns = [

    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('new=/',views.new,name='new'),
    path('submit/',views.submit,name='submit'),
    path('sub/',views.sub,name='sub')
]