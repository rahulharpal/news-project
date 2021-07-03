from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsapp/index.html')

def sportsinfo(request):
    head='Sports news '
    msg1='Kohli made century'
    msg2='India beat england with 2-0'
    msg3='Sachin tendulkar retired from cricket'
    my_dict={'head':head,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def moviesinfo(request):
    head='Movies masala news '
    msg1='Bahubali 3 going to release'
    msg2='Salman ready to get marriage'
    msg3='Anushka and kohli going to marriage soon'
    my_dict={'head':head,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def politicsinfo(request):
    head='Politics news '
    msg1='BJP win west bengal election'
    msg2='Rahul gandhi to be next PM'
    msg3='Amit shah rally going to be conduct in WB on this saturady'
    my_dict={'head':head,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
