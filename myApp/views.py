from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

def sayhello(request):
    return HttpResponse('sayhello.......')

def hello2(request,username):
    now = datetime.now()
    return render(request,'hello3.html',locals())

def hello4(request,username):
    now = datetime.now()
    return render(request,'hello4.html',locals())
    
def test_dict(request):
    dict1 = {'key1':123, 'key2':456}
    return render(request,'hello4.html',locals())

def dice(request):
    no = random.randint(1,6)
    return render(request,"dice.html",{"no":no})

def dice2(request):
   no1=random.randint(1,6)   # 1~6
   no2=random.randint(1,6)   # 1~6
   no3=random.randint(1,6)   # 1~6
   # 使用 locals()傳遞所有的區域變數 
   return render(request,"dice2.html",locals())   

times=0
def dice3(request):
   global times      # 宣告 global 變數
   times = times + 1
   local_times=times # 指派給 區域變數 local_times
   username="David"
   dict_no={"no":random.randint(1,6)}   # 1~6   
   return render(request,"dice3.html",locals())

def show(request):
    person1={"name":"Marcy Abadree","phone":"20100517-0112","age":1004}
    person2={"name":"Bonnibel","phone":"20100823-0122","age":888}
    person3={"name":"Simon Petrikov","phone":"20140224-0548","age":1046}
    persons=[person1, person2, person3]
    
    # TODO 9*9 multiplication table
    row_list = []
    col_list = []
    for i in range(1, 10):
        for j in range(1, 10):
            col_list.append(f'{j} x {i} = {j*i}')
        row_list.append(col_list)
    
    return render(request, "show.html", locals())

def filter(request):
    value=4
    list1=[1,2,3]
    pw="芝麻開門"
    
    html="<h1>Hello</h1>"
    value2=False
    return render(request,"filter.html",locals()) 
