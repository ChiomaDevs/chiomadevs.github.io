from django import forms

from django.shortcuts import render

# Create your views here.

tasks = ["Laundry", "Cook", "Dishes"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    priority = forms.IntegerField(label= "Priority", min_value= 1, max_value=10 )
    date = forms.DateField(label="Today's Date", 
                           widget=forms.SelectDateWidget(attrs={
                               'style': 'margin: 5px; padding: 10px; font-size"16px; border-radius:5px; border: 1px;'
                           })
                           )

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    } )

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })