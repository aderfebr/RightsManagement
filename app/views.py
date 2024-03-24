from django.http import JsonResponse
from app.models import User,Menu,Token
import hashlib,datetime

def menu(request):
    res=list(Menu.objects.all().values())
    return JsonResponse(res,safe=False)

def user(request):
    res=list(User.objects.all().values())
    return JsonResponse(res,safe=False)

def add_salt(text):
    salt=text[:5]
    md=hashlib.md5((str(text).join(salt)).encode())
    password=md.hexdigest()
    return password

def register(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    groupid=request.POST.get("groupid")
    groupname=request.POST.get("groupname")
    if User.objects.filter(username=username):
        return JsonResponse({
        'code':403,
        'msg':'用户已存在',
        })
    else:
        password=add_salt(password)
        User.objects.create(username=username,password=password,groupid=groupid,groupname=groupname)
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
            'msg':'密码错误',
            })
    else:
        return JsonResponse({
        'code':403,
        'msg':'用户不存在',
        })

def logout(request):
    token=request.POST.get("token")
    Token.objects.filter(value=token).delete()
    return JsonResponse({
    'code':200,
    'msg':'登出成功',
    })

def changepwd(request):
    userid=request.POST.get("userid")
    oldpwd=request.POST.get("oldpwd")
    newpwd=request.POST.get("newpwd")
    try:
        user=User.objects.get(userid=userid,password=add_salt(oldpwd))
        user.password=add_salt(newpwd)
        user.save()
        Token.objects.filter(userid=user.userid).delete()
        return JsonResponse({
        'code':200,
        'msg':'更改成功',
        })
    except User.DoesNotExist:
        return JsonResponse({
        'code':403,
        'msg':'密码错误',
        })
    
def deleteuser(request):
    userid=request.POST.get("userid")
    User.objects.get(userid=userid).delete()
    Token.objects.filter(userid=userid).delete()
    return JsonResponse({
    'code':200,
    'msg':'更改成功',
    })