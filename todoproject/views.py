from django.http import HttpResponse

def home(request):
    return HttpResponse("Добро пожаловать в Todo App! \n http://127.0.0.1:8000/api/users/token/ \n ")
