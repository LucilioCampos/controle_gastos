from django.urls import path
from contas.views import home, listagem, novaTransacao, editar, delete

urlpatterns = [
    path('home', home),
    path('listagem', listagem, name='url_listagem'),
    path('form', novaTransacao, name='url_nova'),
    path('update/<int:pk>/', editar, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
]
