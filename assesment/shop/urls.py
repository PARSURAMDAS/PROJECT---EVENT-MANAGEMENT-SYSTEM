from django.urls import path
from .views import *
urlpatterns= [
    path('',home,name='home'),
    path('adminlog',adminlog,name='adminlog'),
    path('userlog',userlog,name='userlog'),
    path('userreg',userreg,name='userreg'),
    path('adminlanding',adminlanding,name='adminlanding'),
    path('customerlanding',customerlanding,name='customerlanding'),
    path('events',enterevent,name='enterevent'),
    path('showevent',showevent,name='showevent'),
    path('deleteevent',deleteevent,name='deleteevent'),
    path('editevent',editevent,name='editevent'),
    path('allevent',allevent,name='allevent'), 
    path('orderevent<pk>',orderevent,name='orderevent'),
    path('showeventorder',showeventorder,name='showeventorder'),
    path('cancelorderevent',cancelorderevent,name='cancelorderevent'),
    path('logout',logout,name='logout'),
    path('resetpassword',reset_password,name='reset_password'),

]