from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request, "burger_list.html")