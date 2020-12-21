from django import forms
from blog.models import post,Comment

class Contactform(forms.Form):
    countries = [("IN","INDIA"),("USA","AMERICA")]
    name = forms.CharField()
    email = forms.EmailField(required=False)
    phone = forms.RegexField(regex="^[6-9][0-9]{9}$",required=False)
    message = forms.CharField(max_length=500)
    country = forms.ChoiceField(choices=countries)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        if email == '' and phone == '':
            raise forms.ValidationError("Atleast email or phone number should be provided" ,code= "invalid")

class Postform(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":70}))
    author = forms.CharField(disabled=True)
    class Meta:
        model = post
        fields = ["title","content","category","image","status","date",]

class Searchform(forms.Form):
    search = forms.CharField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')