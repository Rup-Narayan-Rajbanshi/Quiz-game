
from django.urls import path
from .views import *
# from apis.views import *

app_name = 'user'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/',register_view, name='register'),
    path('update/<int:id>/',user_update_view,name='update'),
]