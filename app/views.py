from django.http import JsonResponse
from app.models import User,Menu,Token
import hashlib,datetime

def menu(request):
    menu=list(Menu.objects.all().values())
    print(menu)
    return JsonResponse(menu,safe=False)

def add_salt(text):
    salt=text[:5]
    md=hashlib.md5((str(text).join(salt)).encode())
    password=md.hexdigest()
    return password

def register(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    if User.objects.filter(username=username):
        return JsonResponse({
        'code':403,
        'msg':'用户已存在',
        })
    else:
        password=add_salt(password)
        User.objects.create(username=username,password=password)
        return JsonResponse({
            'code':200,
            'msg':'注册成功',
        })

def login(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    if User.objects.filter(username=username):
        password=add_salt(password)
        try:
            user=User.objects.get(username=username,password=password)
            token=add_salt(username)
            Token.objects.create(userid=user.userid,value=token,expire_date=datetime.datetime.now()+datetime.timedelta(days=1))
            return JsonResponse({
            'code':200,
            'msg':'登陆成功',
            'username':user.username,
            'token':token,
            })
        except User.DoesNotExist:
            return JsonResponse({
            'code':403,
            'msg':'登录失败',
            })
    else:
        return JsonResponse({
        'code':403,
        'msg':'用户不存在',
        })