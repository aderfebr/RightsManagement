from django.http import JsonResponse
from app.models import Group,GroupRights,Menu,Rights,Token,User,UserGroup
import hashlib,datetime,json

def getauth(token,auth):
    try:
        data=Token.objects.get(value=token)
        userid=data.userid
        if datetime.datetime.now()>data.expire_date.replace(tzinfo=None):
            return False
    except:
        return False
    try:
        group=list(UserGroup.objects.filter(userid=userid).values())
    except:
        return False
    for groupid in group:
        rights=list(GroupRights.objects.filter(groupid=groupid['groupid']).values())
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
            Token.objects.filter(userid=user.userid).delete()
            token=add_salt(username+str(datetime.datetime.now()))
            Token.objects.create(userid=user.userid,value=token,expire_date=datetime.datetime.now()+datetime.timedelta(days=1))
            return JsonResponse({
            'code':200,
            'msg':'登陆成功',
            'username':user.username,
            'token':token,
            })
        except:
            return JsonResponse({
            'code':403,
            'msg':'密码错误',
            })
    else:
        return JsonResponse({
        'code':403,
        'msg':'用户不存在',
        })

def getuser(request):
    token=request.POST.get("token")
    filter=request.POST.get("filter")
    page=int(request.POST.get("page"))
    if getauth(token,1):
        if filter is None:
            res=User.objects.all()
        else:
            res=User.objects.filter(username__contains=filter)
        res=res[page*10-10:page*10]
        total=User.objects.count()
        return JsonResponse({
            'data':list(res.values()),
            'total':total//10+(total%10!=0),
            'code':200,
            'msg':'查询用户成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def adduser(request):
    username=request.POST.get("username")
    age=request.POST.get("age")
    address=request.POST.get("address")
    token=request.POST.get("token")
    if getauth(token,2):
        User.objects.create(username=username,age=age,address=address)
        return JsonResponse({
            'code':200,
            'msg':'修改用户成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def edituser(request):
    userid=request.POST.get("userid")
    age=request.POST.get("age")
    address=request.POST.get("address")
    token=request.POST.get("token")
    if getauth(token,3):
        User.objects.filter(userid=userid).update(age=age,address=address)
        return JsonResponse({
            'code':200,
            'msg':'修改用户成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def changepwd(request):
    userid=request.POST.get("userid")
    oldpwd=request.POST.get("oldpwd")
    newpwd=request.POST.get("newpwd")
    token=request.POST.get("token")
    if getauth(token,3):
        try:
            user=User.objects.get(userid=userid,password=add_salt(oldpwd))
            user.password=add_salt(newpwd)
            user.save()
            Token.objects.filter(userid=user.userid).delete()
            return JsonResponse({
            'code':200,
            'msg':'修改密码成功，请重新登录',
            })
        except:
            return JsonResponse({
            'code':403,
            'msg':'密码错误',
            })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def getgroupbyuser(request):
    userid=request.POST.get("userid")
    token=request.POST.get("token")
    if getauth(token,4):
        user=UserGroup.objects.filter(userid=userid).values()
        group=[]
        for i in user:
            group.append(int(i["groupid"]))
        res=list(Group.objects.all().values())
        return JsonResponse({
            'data':res,
            'group':group,
            'code':200,
            'msg':'查询角色权限成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })
    
def editgroupbyuser(request):
    userid=request.POST.get("userid")
    group=request.POST.get("group")
    group=json.loads(group)
    token=request.POST.get("token")
    if getauth(token,4):
        UserGroup.objects.filter(userid=userid).delete()
        for i in group:
            UserGroup.objects.create(userid=userid,groupid=i)
        return JsonResponse({
            'code':200,
            'msg':'修改用户角色成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })    

def deleteuser(request):
    userid=request.POST.get("userid")
    token=request.POST.get("token")
    if getauth(token,5):
        User.objects.get(userid=userid).delete()
        Token.objects.filter(userid=userid).delete()
        return JsonResponse({
        'code':200,
        'msg':'删除用户成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def getgroup(request):
    token=request.POST.get("token")
    filter=request.POST.get("filter")
    page=int(request.POST.get("page"))
    if getauth(token,1):
        if filter is None:
            res=Group.objects.all()
        else:
            res=Group.objects.filter(username__contains=filter)
        res=res[page*10-10:page*10]
        total=Group.objects.count()
        return JsonResponse({
            'data':list(res.values()),
            'total':total//10+(total%10!=0),
            'code':200,
            'msg':'查询角色成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def addgroup(request):
    groupname=request.POST.get("groupname")
    token=request.POST.get("token")
    if getauth(token,7):
        try:
            Group.objects.create(groupname=groupname)
            return JsonResponse({
                'code':200,
                'msg':'增加用户成功',
            })
        except:
            return JsonResponse({
                'code':403,
                'msg':'主键重复',
            })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def editgroup(request):
    groupid=request.POST.get("groupid")
    groupname=request.POST.get("groupname")
    token=request.POST.get("token")
    if getauth(token,8):
        Group.objects.filter(groupid=groupid).update(groupname=groupname)
        return JsonResponse({
            'code':200,
            'msg':'修改用户成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def getrights(request):
    groupid=request.POST.get("groupid")
    token=request.POST.get("token")
    if getauth(token,9):
        group=GroupRights.objects.filter(groupid=groupid).values()
        rights=[]
        for i in group:
            rights.append(int(i["rightsid"]))
        res=list(Rights.objects.all().values())
        return JsonResponse({
            'data':res,
            'rights':rights,
            'code':200,
            'msg':'查询角色权限成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def editrights(request):
    groupid=request.POST.get("groupid")
    rights=request.POST.get("rights")
    rights=json.loads(rights)
    token=request.POST.get("token")
    if getauth(token,9):
        GroupRights.objects.filter(groupid=groupid).delete()
        for i in rights:
            GroupRights.objects.create(groupid=groupid,rightsid=i)
        return JsonResponse({
            'code':200,
            'msg':'修改角色权限成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def deletegroup(request):
    groupid=request.POST.get("groupid")
    token=request.POST.get("token")
    if getauth(token,10):
        Group.objects.get(groupid=groupid).delete()
        return JsonResponse({
        'code':200,
        'msg':'删除角色成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })

def getmenu(request):
    res=list(Menu.objects.all().values())
    return JsonResponse(res,safe=False)

def editmenu(request):
    index=request.POST.get("index")
    token=request.POST.get("token")
    if getauth(token,7):
        index=json.loads(index)
        for i in index:
            Menu.objects.filter(id=i["id"]).update(vis=i["vis"])
        return JsonResponse({
            'code':200,
            'msg':'修改菜单成功',
        })
    else:
        return JsonResponse({
            'code':403,
            'msg':'未授权',
        })
