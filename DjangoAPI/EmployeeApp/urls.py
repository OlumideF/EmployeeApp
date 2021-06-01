from django.conf.urls import url
from EmployeeApp import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns=[
    url(r'^department/$',views.DepartmentAPI),
    url(r'^department/([0-9]+)$', views.DepartmentAPI),
    
    url(r'^employee/$',views.EmployeeAPI),
    url(r'^employee/([0-9]+)$', views.EmployeeAPI),

    url(r'^SaveFile$', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)