from django.urls import path
from . import views  # can have some other dependency to other module name views

# /products
# /products/new
urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('show/', views.show_products),
    path('run/', views.dump_model),
    path('getValues/', views.run_model)
    # path('showFiles/', views.show_files)
]
