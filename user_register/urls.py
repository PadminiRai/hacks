from django.urls import path,include
from . import views
from .views import *
urlpatterns = [
    # path('',views.employee_form ),
    path('list/',views.employee_list ),
    path('homepagef/',homepagef,name='homepagef'),
    path('addv/',addv,name='addv'),
    path('addc/',addc,name='addc'),    
    path('charityregisterf/',charityregisterf,name='charityregisterf'),
    path('event_regf/',event_regf,name='event_regf'),
    path('event_addf/',event_addf,name='event_addf'),
    path('v_eventf/',v_eventf,name='v_eventf'),
   
]