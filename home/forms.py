from django import forms


class ContactForm(forms.Form):
    """Generates contact form"""
    first_name = forms.CharField(
            max_length=50, widget=forms.TextInput(
                attrs={'placeholder': 'First name'})
        )
    last_name = forms.CharField(
            max_length=50, widget=forms.TextInput(
                attrs={'placeholder': 'Last name'})
        )
    email_address = forms.EmailField(
            max_length=150, widget=forms.TextInput(
                attrs={'placeholder': 'Email'}))
    message = forms.CharField(
            widget=forms.Textarea(
                attrs={'placeholder': 'Your message'})
        )
