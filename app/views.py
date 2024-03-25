from django.http import JsonResponse
from app.models import Group,GroupRights,Menu,Token,User
import hashlib,datetime,json

def getmenu(request):
    res=list(Menu.objects.all().values())
    return JsonResponse(res,safe=False)

def changemenu(request):
    index=request.POST.get("index")
    index=json.loads(index)
    for i in index:
        print(i)
        Menu.objects.filter(id=i["id"]).update(vis=i["vis"])
    return JsonResponse({
        'code':200,
        'msg':'修改菜单成功',
    })

def getauth(token,auth):
    try:
        data=Token.objects.get(value=token)
        userid=data.userid
        if datetime.datetime.now()>data.expire_date.replace(tzinfo=None):
            return False
    except Token.DoesNotExist:
        return False
    try:
        groupid=User.objects.get(userid=userid).groupid
    except User.DoesNotExist:
        return False
    rights=list(GroupRights.objects.filter(groupid=groupid).values())
    for i in rights:
        if i["rightsid"]==auth:
            return True
    return False

def add_salt(text):
    salt=text[:5]
    md=hashlib.md5((text.join(salt)).encode())
    password=md.hexdigest()
    return password

def register(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    groupid=request.POST.get("groupid")
    if User.objects.filter(username=username):
        return JsonResponse({
        'code':403,
        'msg':'用户已存在',
        })
    else:
        password=add_salt(password)
        User.objects.create(username=username,password=password,groupid=groupid,groupname=Group.objects.get(groupid=groupid).groupname)
        return JsonResponse({
            'code':200,
            'msg':'注册成功',
        })
    
def getgroup(request):
    res=list(Group.objects.all().values())
    return JsonResponse(res,safe=False)

def login(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    if User.objects.filter(username=username):
        password=add_salt(password)
        try:
            user=User.objects.get(username=username,password=password)
            Token.objects.filter(userid=user.userid).delete()
            token=add_salt(username+str(datetime.datetime.now()))
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

def getuser(request):
    token=request.POST.get("token")
    if getauth(token,"1"):
        res=list(User.objects.all().values())
        return JsonResponse({
            'data':res,
            'code':200,
            'msg':'查看用户成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def edituser(request):
    userid=request.POST.get("userid")
    username=request.POST.get("username")
    groupid=request.POST.get("groupid")
    User.objects.filter(userid=userid).update(username=username,groupid=groupid,groupname=Group.objects.get(groupid=groupid).groupname)
    return JsonResponse({
        'code':200,
        'msg':'修改用户成功',
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