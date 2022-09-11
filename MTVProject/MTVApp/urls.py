from django.urls import path
from MTVApp.views import *

urlpatterns = [
    path('familiar1/', familiar1),
    path('familiar2/', familiar2),
    path('familiar3/', familiar3),

]
