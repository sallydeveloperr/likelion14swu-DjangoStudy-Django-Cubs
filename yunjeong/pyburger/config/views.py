from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

# #main 함수 정의
# def main(request):
#     return HttpResponse("안녕하세요, pyburger입니다.")
#
# #버거의 종류를 알려주는 직원 역할
# def burger_list(request):
#     return HttpResponse("pyburger의 햄버거 목록입니다.")

def main(request):
    return render(request, "main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    #Template으로 전달해줄 dict 객체
    context = {
        "burgers": burgers, #burgers 키에 burgers 변수(QuerySet 객체)를 전달한다.
    }
    #render 함수의 마지막에 context 전달
    return render(request, "burger_list.html", context)