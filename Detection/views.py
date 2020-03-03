from django.shortcuts import render

# Create your views here.

def index(request):
    mydict={
        "id":"121",
        "Name":"Aiswarya"
    }

    return render(request, "htmlpage.html", context=mydict)
    
def home(request):
    mydict={
        "id":"121",
        "Name":"Aiswarya",
        "course":"MCA"
    }

    return render(request, "student.html", context=mydict)
    