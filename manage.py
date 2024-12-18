# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import path
# from django import forms
# from django.db import models
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject.settings") 
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)



# # models.py
# class Feedback(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     comment = models.TextField()

# # forms.py
# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['name', 'email', 'comment']

# # views.py
# def home(request):
#     return render(request, 'home.html')

# def feedback(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'thanks.html')
#         else:
#             return render(request, 'feedback.html', {'form': form, 'error': 'Please correct the errors below.'})
#     else:
#         form = FeedbackForm()
#         return render(request, 'feedback.html', {'form': form})

# # urls.py
# urlpatterns = [
#     path('', home, name='home'),
#     path('feedback/', feedback, name='feedback'),
# ]

