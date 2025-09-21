from django.shortcuts import render


# Create your views here.
def deep_learning_table_view(request):
    return render(request, "deep_learning_table.html")
