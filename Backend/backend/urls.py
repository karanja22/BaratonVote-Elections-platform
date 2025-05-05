
from django.contrib import admin
from django.urls import path, include

from users.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),     
    path('', home, name='home'),   
    # path('api/candidates/', include('candidates.urls')),  
    # path('api/elections/', include('elections.urls')),   
    # path('api/results/', include('results.urls')),        
]