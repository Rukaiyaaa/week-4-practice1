from django import forms
from django.forms.widgets import NumberInput
import datetime
from django.core import validators


class ExampleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        if len(valname) < 10:
            raise forms.ValidationError("Enter a name with at least 10 characters")  


    comment = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    value = forms.DecimalField()
    email_address = forms.EmailField( 
        required = False,
    )
    message = forms.CharField(
	    max_length = 10,
    )
    email_address = forms.EmailField( 
        label="Please enter your email address",
    )
    first_name = forms.CharField(initial='Your name')
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    roll_number = forms.IntegerField( 
        help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput()) 
    file = forms.FileField()
    image = forms.ImageField(label='Upload an Image')

    file1 = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='file Extension must be ended with .pdf')])
