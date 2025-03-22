"""Tests for complaint app forms."""
import pytest
from complaints.forms import ComplaintForm
def test_complaint_form_valid():
    """Test that ComplaintForm is valid with all required fields."""
    form = ComplaintForm(data={
        'title': 'Late delivery',
        'description': 'Order took 2 hours to arrive',
        'email': 'user@example.com',
        'category': 'SV',
        'priority': 'HI',
    })
    assert form.is_valid()
def test_complaint_form_invalid_missing_fields():
    """Test that ComplaintForm is invalid when required fields are missing."""
    form = ComplaintForm(data={
        'title': 'Missing description'
    })
    assert not form.is_valid()  # Should fail due to missing required fields