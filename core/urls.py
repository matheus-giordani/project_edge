"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from devices import views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
router.register(r'peaple', views.PeapleView)
router.register(r'devices', views.DevicesView)
router.register(r'devices_control', views.DevicesControlView)

schema_view = get_swagger_view(title='Documentation')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url('documentation/', schema_view)
    
]



# from django.contrib import admin
# from django.urls import path, include



# from rest_framework import routers
# from devices import views

# router = routers.DefaultRouter()
# router.register(r'peaple', views.PeapleView)
# router.register(r'devices', views.DevicesView)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('admin/', admin.site.urls),
    
# ]