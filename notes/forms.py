from django import forms
from django.forms import ModelForm
from .models import BasicNote, ScheduleBlock


class BasicNoteForm(ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={"id" : "image_field"}), required=False)
    until = forms.DateTimeField(widget=forms.DateTimeInput(format='%D/%M/%Y %H:%M', attrs={'type': 'datetime-local'}),
                              required=False, label="Date")
    desc = forms.CharField(required=False, label="Description")

    class Meta:
        model = BasicNote
        fields = ['name', 'desc', 'image', 'until', 'color']
        widgets = {
            #'until': forms.DateTimeInput(format='%D/%M/%Y %H:%M', attrs={'type': 'datetime-local'}),
            'color': forms.TextInput(attrs={'type': 'color'})
        }


class ScheduleBlockForm(ModelForm):
    endTime = forms.TimeField(label="End Time", widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}), required=False)

    class Meta:
        model = ScheduleBlock
        fields = ['day', 'name', 'startTime', 'endTime', 'color']
        widgets = {
            'startTime': forms.TimeInput(attrs={'type': 'time'}),
            'color': forms.TextInput(attrs={'type': 'color'}),
        }