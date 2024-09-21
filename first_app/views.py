from django.shortcuts import render
from first_app.forms import ExampleForm


# Create your views here.

def djangoForm(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid(): 
            print(form.cleaned_data)
            return render(request, 'home.html', {'form': form})
    else:
        form = ExampleForm()
    return render(request, 'home.html', {'form': form})


def home(request):
    return render(request, 'home.html')