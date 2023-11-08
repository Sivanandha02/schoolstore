from django import forms
from .models import Department, Course

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select a department")
    course = forms.ModelChoiceField(queryset=Course.objects.none(), empty_label="Select a course")

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id)
            except (ValueError, TypeError):
                pass
        elif self.instance and self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set

