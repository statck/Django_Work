from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

# def first_page(request):
#     return HttpResponse("主页")
# 根据app注册的顺序，逐个去对应的app路径下去找template路径下对应的html文件
def user_list(request):
    return render(request, "user_list.html")

def user_add(request):
    return render(request, "user_add.html")

def tpl(request):
    name = "汉朝"
    rolers = ["管理员","CEO","保安"]
    user_info = {
        "name":"郭超",
        "age":20,
        "roler":"CEO"
    }
    data_list = [
        {
            "name": "郭超",
            "age": 20,
            "roler": "CEO"
        },
        {
            "name": "路西",
            "age": 20,
            "roler": "CEO"
        },
        {
            "name": "过阿萨德",
            "age": 20,
            "roler": "CEO"
        }
    ]
    return render(request , "tpl.html", {"n1":name , "n2":rolers , "n3":user_info , "n4":data_list})

def news(request):
    # 1. 定义一些新闻  或者 取数据库取  网络请求取联通获取

    return render(request , "news.html")

def something(request):
    # request是一个对象，封装了用户通过浏览器发送过来的所有数据、
    # 1. 获取请求方式，GET/METHOD
    print(request.method)

    # 2. 在url上传递值，/something/?n1=1234&n2=999
    print(request.GET)

    # 3. 在请求中提交数据
    print(request.POST)

    # 4. HttpResponse("返回内容"),内容字符串返回给请求者
    # return render(request , "news.html")
    # return HttpResponse("返回内容")

    # 5. django读取 + 渲染 + --> 字符串，返回给用户浏览器
    # 6. 让浏览器重定向
    return redirect("https://www.baidu.com")

def login(request):
    if request.method=="GET":
        return render(request , "login.html")
    else:
        # 如果是POST请求，获取用户提交的数据
        # print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")

        if username == "root" and password == "!234":
            return HttpResponse("登录成功")
        else:
            msg = "账户/密码输出出错，请重新输入"
            return render(request , "login.html" , {"err" : msg})

        # return HttpResponse("登录成功")
