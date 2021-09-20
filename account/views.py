from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = ''
        password = request.POST['password']

        # DB内のユーザー名を確認
        try:
            # 合致するユーザーがあればerrorを返す
            User.objects.get(username = username)
            return render(request, 'account/signup.html', {'error':'このユーザー名はすでに使用されています'})
        except:
            # 合致するユーザーがなければDBに登録
            User.objects.create_user(username, email, password)

    return render(request, 'account/signin.html')


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # DB確認
        user = authenticate(request, username = username, password = password)
        if user is not None:
            # DB内にユーザーが存在する場合
            login(request, user)
            return redirect('app:top')
        else:
            # DB内にユーザーが存在しない場合
            return render(request, 'account/signin.html', {'error':'ユーザー名またはパスワードが間違っています'})

    return render(request, 'account/signin.html')

def signout(request):
    logout(request)
    return redirect('account:signin')