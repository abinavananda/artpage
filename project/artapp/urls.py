from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('',views.index,name='index'),
path('about/', views.about_view, name='about'),
path('service/', views.service_view, name='service'),
path('contact/', views.contact_view, name='contact'),
path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



