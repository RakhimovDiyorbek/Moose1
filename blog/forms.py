from .models import Contact, Comment, Subsription

from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # for kalit, qiymat in self.fields.items():
        #      qiymat.witget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['blog']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)


class SubscriptionForms(forms.ModelForm):
    class Meta:
        model = Subsription
        fields = '__all__'
