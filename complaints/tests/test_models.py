"""Tests for complaint app models."""
from django.contrib.auth.models import User
from complaints.models import Complaint
import pytest
@pytest.mark.django_db
def test_create_complaint():
    """Test creating a Complaint object and verifying its attributes."""
    user = User.objects.create_user(username='testuser', password='password')
    complaint = Complaint.objects.create(
        user=user,
        title="Test Complaint",
        description="This is a test complaint."
    )
    assert complaint.get_status_display() == "Pending"
    assert complaint.title == "Test Complaint"
    assert str(complaint) == "Test Complaint"  # Assumes __str__ returns title