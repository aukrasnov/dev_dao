"""wordcount URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('dogdog/', admin.site.urls),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about')
]

export AIRFLOW_HOME=/opt/airflow/airflow
n = 1
for i in range(1):
    airflow test mkt_sessions sessions_tmp 2019-05-24T00:00:00
    print('sessions_tmp Done')
    airflow test mkt_sessions mkt_sessions_stg 2019-05-24T00:00:00
    print('sessions_tmp Done')
    airflow test mkt_sessions insert_mkt_campaigns_channels 2019-05-24T00:00:00
    print('sessions_tmp Done')
    airflow test mkt_sessions insert_mkt_sessions 2019-05-24T00:00:00
    print('sessions_tmp Done')
    airflow test mkt_sessions cleanup 2019-05-24T00:00:00
    print('sessions_tmp Done')
    print('round {} finished'.format(n))
    n +=1