from django.shortcuts import render
from .forms import FeedbackForm

def home(request):
    return render(request, 'home.html')

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
        else:
            return render(request, 'feedback.html', {'form': form, 'error': 'Please correct the errors below.'})
    else:
        form = FeedbackForm()
        return render(request, 'feedback.html', {'form': form})
