
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', include('poll.urls')),
    path('accounts/',include ('accounts.urls')),
    path('polls/', include('poll.urls')),
    #path('polls/', login_required(include('poll.urls'))),
    path("admin/", admin.site.urls),
    
]
