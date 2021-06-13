from django.urls import path,include
from . import views
from .views import *
urlpatterns = [
    # path('',views.employee_form ),
    path('list/',views.employee_list ),
    path('homepagef/',homepagef,name='homepagef'),
    path('acceptf/',acceptf,name='acceptf'),
    path('charityregisterf/',charityregisterf,name='charityregisterf'),
    path('event_regf/',event_regf,name='event_regf'),
    path('v_eventf/',v_eventf,name='v_eventf'),
   
]