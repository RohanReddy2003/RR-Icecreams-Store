
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "RR Ice Creams Admin"
admin.site.site_title = "RR Ice Creams Admin Portal"
admin.site.index_title = "Welcome to RR Ice Creams"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls'))
]
