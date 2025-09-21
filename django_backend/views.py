from django.shortcuts import render


# Create your views here.
def django_backend_view(request):
    name = "ismael"
    age = 29
    info = {"name": name, "age": age}
    return render(request, "django_backend.html", context=info)
