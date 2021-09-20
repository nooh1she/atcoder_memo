from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [

    #サインアップ
    path('signup/', views.signup, name = 'signup'),

    #サインイン
    path('signin/', views.signin, name = 'signin'),

    #サインアウト
    path('signout/', views.signout, name = 'signout'),
    

]