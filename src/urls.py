from django.urls import path
from . import views

urlpatterns = [

        path('', views.categoryList),
        path('create/', views.createCategory),
        path('detail/<int:id>/', views.detailCategory),
        path('update/<int:id>/', views.updateCategory),
        path('delete/<int:id>/', views.deleteCategory),


]