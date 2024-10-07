"""
URL configuration for assesment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from shop import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',include('shop.urls')),
    path('admin/', admin.site.urls),
    path('',views.home),
    path('adminlog/',views.adminlog),
    path('userlog/',views.userlog),
    path('userreg/',views.userreg),
    path('adminlanding/',views.adminlanding),
    path('customerlanding/',views.customerlanding),
    path('event/',views.enterevent),
    path('showevent/',views.showevent),
    path('deleteevent/<int:eventid>/',views.deleteevent),
    path('editevent/<int:eventid>/',views.editevent),
    path('allevent/<int:eventid>/',views.allevent),
    path('showevent/',views.showevent),
    path('orderevent/<int:ordereventid>/',views.orderevent),
    path('showorderevent/',views.showeventorder),
    path('cancelorderevent/<int:ordereventid>',views.cancelorderevent),
    path('logout/',views.logout),
    path('resetpassword/',views.reset_password),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
