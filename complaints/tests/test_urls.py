"""Tests for URL resolution in the complaints app."""
from django.urls import reverse, resolve
from complaints.views import submit_complaint, user_dashboard
def test_submit_complaint_url():
    """Test that the submit_complaint URL resolves correctly."""
    url = reverse('submit_complaint')
    assert resolve(url).func == submit_complaint
def test_user_dashboard_url():
    """Test that the user_dashboard URL resolves correctly."""
    url = reverse('user_dashboard')
    assert resolve(url).func == user_dashboard