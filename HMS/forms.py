from django import forms
from .models import Record

class RecordCreateForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

    def clean_room_number(self):
        room_number = self.cleaned_data.get('room_number')
        if not room_number:
            raise forms.ValidationError('This field is required')
        for instance in Record.objects.all():
            if instance.room_number == room_number:
                raise forms.ValidationError('Room already taken')    
        return room_number


class RecordSearchForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['room_number', 'occupant_name']  

class RecordUpdateForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
