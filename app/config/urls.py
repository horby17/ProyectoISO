
from django.contrib import admin
from django.urls import path, include

from core.views import firstview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', include('core.urls'))
]
