from atcoder_memo.atcoder_memo.app.views import modify_problem, move_modify
from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [

    #トップページ
    path('', views.top, name = 'top'),

    #問題の登録画面への遷移
    path('move_create/', views.submit, name = 'move_create'),
    #問題の登録フォーム
    path('create/', views.create_problem, name = 'create'),


    #問題の編集画面への遷移
    path('move_modify/', views.move_modify, name = 'move_modify'),
    #問題の編集画面
    path('modify/', views.modify_problem, name= 'modify'),


    #問題の一覧画面
    path('items/', views.items_problem, name = 'items'),

    #問題の閲覧・検索
    #path('items', views.items, name = 'items')

]