from django import forms
from posts.models import Post, Comment

BANNED_WORDS = ("war", "BEGIN",)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "image", "category")

    def clean_title(self):
        title = self.cleaned_data["title"]

        if title in BANNED_WORDS:
            raise forms.ValidationError("Title has banned word!")

        return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author_name", "text")

    