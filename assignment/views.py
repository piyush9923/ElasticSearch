from django import forms
from django.shortcuts import render, HttpResponse
from .models import Feedback_Form

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    rate_train = forms.ChoiceField(widget=forms.RadioSelect,
                                   choices=(('Poor', 'Poor'), ('Average', 'Average'), ('Excellent', 'Excellent')), label="How would you rate the training?")
    checkbox = forms.ChoiceField(widget=forms.CheckboxSelectMultiple,
                                 choices=(('Venue', 'Venue'), ('Trainer', 'Trainer'), ('Materials', 'Materials')), label="What could be improved?")
    feedback = forms.CharField(widget=forms.Textarea, label="Any special mentions/future inclusions/ complaints?")


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mail = request.POST.get('email')
        rate = request.POST.get('rate_train')
        check = request.POST.getlist('checkbox')
        feed = request.POST.get('feedback')
        query = Feedback_Form(name=name, email=mail, rate=rate, check=check, feed=feed)
        query.save()
        return render(request, "assignment/response.html")
    else:
        form = FeedbackForm()
        return render(request, "assignment/index.html", {
            "form": form
        })