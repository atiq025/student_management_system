from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__' 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label.lower()}",
            })


    
