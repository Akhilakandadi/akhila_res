"""Forms for the complaints app, including complaint submission and user registration."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Complaint
class ComplaintForm(forms.ModelForm):
    """Form for creating and editing Complaint objects."""
    class Meta:
        """Metadata for ComplaintForm specifying model and fields."""
        model = Complaint
        fields = ['title', 'description', 'email', 'category', 'priority', 'image', 'is_urgent']
    def clean_title(self):
        """Ensure title is at least 5 characters long."""
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise ValidationError('Title must be at least 5 characters long.')
        return title
    def clean_description(self):
        """Ensure description is at least 10 characters long."""
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise ValidationError('Description must be at least 10 characters long.')
        return description
    def clean_email(self):
        """Ensure email is provided for all complaints."""
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Email is required for all complaints.')
        return email
    def clean_image(self):
        """Validate image file size is under 2MB."""
        image = self.cleaned_data.get('image')
        if image and image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError('Image file size must be less than 2MB.')
        return image
    def clean(self):
        """Cross-field validation: Urgent complaints must have High priority."""
        cleaned_data = super().clean()
        is_urgent = cleaned_data.get('is_urgent')
        priority = cleaned_data.get('priority')
        if is_urgent and priority != 'HI':
            self.add_error('priority', 'Urgent complaints must have High priority.')
        return cleaned_data
class UserRegistrationForm(UserCreationForm):
    """Form for registering new users with email."""
    email = forms.EmailField()
    class Meta:
        """Metadata for UserRegistrationForm specifying model and fields."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']
