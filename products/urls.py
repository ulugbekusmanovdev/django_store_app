from django.urls import path
from . import views

app_name='products'
urlpatterns = [
    path('new', views.new_product, name='new'),
    path('<int:product_id>/detail', views.product_detail, name='detail'),
    path('<int:product_id>/update', views.product_update, name='update'),
    path('<int:product_id>/delete', views.product_delete, name='delete'),
    path('<int:product_id>/comment/new', views.new_comment, name='new_comment'),
    path('<int:product_id>/comment/<int:comment_id>/delete', views.delete_comment, name='comment_delete'),
]