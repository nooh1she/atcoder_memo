from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [

    #トップページ
    path('', views.top, name='top'),

    #問題の登録
    path('submit/', views.submit, name='submit'),

    #問題の閲覧・検索
    #path('items', views.items, name = 'items')

]