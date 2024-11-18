
from django.urls import path
from . import views

#localhost:800/chai
urlpatterns = [
    
    path('',views.all_chai,name='all_chai'),
    path('<int:chai_id>/', views.chai_deatail, name='chai_detail'),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),

   
    
    
]