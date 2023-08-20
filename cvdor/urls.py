from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('parcelas', views.all_parcelas, name='all-parcelas'),
    path('show_parcela/<parcela_id>', views.show_parcela, name='show-parcela'),
    path('update_parcela/<parcela_id>', views.update_parcela, name='update-parcela'),
]
