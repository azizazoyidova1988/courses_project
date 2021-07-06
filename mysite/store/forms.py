from django import forms
from store.models import Commenter, Subscribe, Course, Team, News,Video,Items


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe()
        fields = '__all__'


class CommenterForm(forms.ModelForm):
    class Meta:
        model = Commenter()
        fields = '__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News()
        fields = '__all__'


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team()
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course()
        fields = '__all__'


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video()
        fields = '__all__'


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items()
        fields = '__all__'