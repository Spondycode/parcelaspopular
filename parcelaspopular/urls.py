from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cvdor.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

admin.site.site_header = "Parcelas Administration"
admin.site.site_title = "Spondy Club"
admin.site.index_title = "Making Changes!"
