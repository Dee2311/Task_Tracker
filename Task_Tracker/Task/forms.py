from django import forms
from django.contrib.auth.models import User
from .models import AddList, AddTask



def widget_attrs(placeholder):
    return {'class': 'u-full-width', 'placeholder': placeholder}


def form_kwargs(widget, label='', max_length=64):
    return {'widget': widget, 'label': label, 'max_length': max_length}


class LoginForm(forms.Form):

    username = forms.CharField(
        **form_kwargs(widget=forms.TextInput(attrs=widget_attrs('Username')))
    )
    password = forms.CharField(
        **form_kwargs(
            widget=forms.PasswordInput(attrs=widget_attrs('Password'))
        )
    )

class ListForm(forms.Form):
    listName = forms.CharField(
        **form_kwargs(widget=forms.TextInput(attrs=widget_attrs('listName')))
    )
  

class TaskForm(forms.Form):

    title = forms.CharField(
        **form_kwargs(widget=forms.TextInput(attrs=widget_attrs('Title')))
    )

    description = forms.CharField(
        **form_kwargs(widget=forms.Textarea(
            attrs=widget_attrs('Description')))
    )

    expected_time = forms.TimeField(input_formats = ['%H:%M'])
    

    due_date = forms.DateField()

    CHOICES = (
        (1, 'Unassigned'),
        (2, 'Pending'),
        (3, 'Accepted'),
        (4, 'Started'),
        (5, 'Completed'),
    )
   
    status = forms.ChoiceField(choices=CHOICES)



