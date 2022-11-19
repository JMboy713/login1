from django.shortcuts import render
from django.http import HttpResponse

from django.utils.datastructures import MultiValueDictKeyError


def login(request): #get방식으로 받는 경우
    user_data={
        'username' : 'jimin713',
        'password': 'wlals980713'
    }

    if (request.method=="GET"):
            return render(request,'users/login.html')
         #로그인 화면을 유저가 url을 직접 입력해서 들어갈때 처리하는 것.
        #if username is None and password is None:
              #  return render(request,'users/login.html')
        #elif username is None or password is None:
               # return HttpResponse('불가능한 접근입니다.')


    #POST           
    if (request.method=='POST'):        

        username=request.POST.get('username')
        password=request.POST.get('password')
           
            #로그인 화면에서 유저가 아이디 비밀번호를 입력해서 들어갈때 blank일때 
            #실수로 입력을 다 못했을 경우를 대비
        if username=='':
                return HttpResponse('유저아이디를 입력해주세요')
        if password =='':
                return HttpResponse('유저 비밀번호를 입력해주세요.')
        
            #아이디 중 비밀번호가 틀렸을때 
        if (username!=user_data['username']):
                return HttpResponse('유저 아이디가 올바르지 않습니다.')
            
        if(password!=user_data['password']):
                return HttpResponse("유저 비밀번호가 올바르지 않습니다.")

        return HttpResponse('로그인성공')

    return HttpResponse()


