from django.shortcuts import render


# Create your views here.
def machine_learning_view(request):
    return render(request, "machine_learning.html")
