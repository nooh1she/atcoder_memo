from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [

    #トップページ
    path('', views.top, name = 'top'),

    #問題の登録画面への遷移
    path('create/', views.create, name = 'create'),
    #問題の登録フォーム
    path('done_create/', views.done_create, name = 'done_create'),


    #問題の編集画面への遷移
    path('modify/<int:pk>/', views.modify, name = 'modify'),
    #問題の編集画面
    path('done_modify/<int:pk>/', views.done_modify, name= 'done_modify'),
    
    #問題削除の確認
    path('confirm_delete/<int:pk>/', views.confirm_delete, name = 'confirm_delete'),
    #問題の削除
    path('delete/<int:pk>/', views.delete, name = 'delete'),


    #問題の一覧画面
    path('items/', views.items_problem, name = 'items'),
    #問題の詳細画面
    path('content/<int:pk>/', views.content_problem, name = 'content'),
    #検索結果画面
    path('search/', views.search_problem, name = "search"),

    #ログアウト確認
    path('confirm_signout/', views.confirm_signout, name = 'confirm_signout'),

]