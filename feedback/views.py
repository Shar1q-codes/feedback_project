from django.shortcuts import render, redirect
from .forms import FeedbackForm

def submit_feedback(request):
    success = False
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = FeedbackForm()  # reset the form after saving
    else:
        form = FeedbackForm()
        
    return render(request, 'feedback/submit.html', {'form': form, 'success': success})
