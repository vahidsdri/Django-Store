from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name="product_list"),
    path('', views.HomePage.as_view(), name ="home_page"),
    path('products/<slug:slug>',views.DetailPage.as_view(), name = "detail_page")
]