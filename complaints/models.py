"""Models for the complaints app."""
from django.contrib.auth.models import User
from django.db import models
class Complaint(models.Model):
    """Model representing a user-submitted complaint."""
    # Category Choices
    FOOD = 'FO'
    SERVICE = 'SV'
    CLEANLINESS = 'CL'
    CATEGORY_CHOICES = [
        (FOOD, 'Food'),
        (SERVICE, 'Service'),
        (CLEANLINESS, 'Cleanliness'),
    ]
    # Status Choices
    PENDING = 'PE'
    RESOLVED = 'RE'
    IN_PROGRESS = 'IP'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (RESOLVED, 'Resolved'),
        (IN_PROGRESS, 'In Progress'),
    ]
    # Priority Choices
    HIGH = 'HI'
    MEDIUM = 'ME'
    LOW = 'LO'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]
    # Fields
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    email = models.EmailField(blank=True, null=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    status_updated_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        default=MEDIUM
    )
    image = models.ImageField(
        upload_to='complaints/',
        blank=True,
        null=True
    )
    resolved_at = models.DateTimeField(blank=True, null=True)
    is_urgent = models.BooleanField(default=False)
    resolved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='resolved_complaints'
    )
    def __str__(self):
        """Return the complaint title as a string."""
        return self.title
class StatusHistory(models.Model):
    """Model tracking status changes of a complaint."""
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    old_status = models.CharField(max_length=2, choices=Complaint.STATUS_CHOICES)
    new_status = models.CharField(max_length=2, choices=Complaint.STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return a string showing the complaint title and status change."""
        return f'{self.complaint.title} ({self.old_status} -> {self.new_status})'