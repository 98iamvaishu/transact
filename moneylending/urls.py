"""moneylending URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from transact.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', home, name='home1'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signin1/', signin1, name='signin1'),
    path('logout/', logout1, name='logout'),
    path('test/', test, name='test'),
    path('dashboard/', dashboard, name='create'),
    path('borrow/', borrower, name='borrow'),
    path('list1/', list1, name='list1'),
    path('paid/<int:borrowerid>/', paidfun, name='paid'),
    path('history/<int:borid>/',history,name='history')
]
