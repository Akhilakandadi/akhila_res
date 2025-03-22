"""Views for the complaints app handling registration, complaints, and dashboard."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ComplaintForm
from .models import Complaint
def register(request):
    """Handle user registration and auto-login."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('submit_complaint')
        # Keep the invalid form with errors for rendering below
    else:
        form = UserRegistrationForm()  # Initialize form for GET requests

    return render(request, 'complaints/register.html', {'form': form})
@login_required
def submit_complaint(request):
    """Handle complaint submission for authenticated users."""
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.status = 'PE'
            complaint.save()
            print("Complaint saved successfully!")  # Debugging
            return redirect('complaint_success')
        print("Form errors:", form.errors)  # Debugging
        # Keep the invalid form with errors for rendering below
    else:
        form = ComplaintForm()  # Initialize form for GET requests

    return render(request, 'complaints/submit_complaints.html', {'form': form})
@login_required
def user_dashboard(request):
    """Display the user's complaints in a dashboard."""
    complaints = Complaint.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'complaints/user_dashboard.html', {'complaints': complaints})
@login_required
def edit_complaint(request, complaint_id):
    """Edit an existing complaint if still pending."""
    complaint = get_object_or_404(Complaint, id=complaint_id, user=request.user)
    if complaint.status != 'PE':
        messages.error(request, "You can't edit a complaint that is already being processed.")
        return redirect('user_dashboard')

    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES, instance=complaint)
        if form.is_valid():
            form.save()
            messages.success(request, 'Complaint updated successfully.')
            return redirect('user_dashboard')
        print("Form errors:", form.errors)  # Debugging
        messages.error(request, "There was an issue updating the complaint.")
    else:
        form = ComplaintForm(instance=complaint)  # Initialize form for GET requests

    return render(request, 'complaints/edit_complaint.html', {'form': form, 'complaint': complaint})
@login_required
def delete_complaint(request, complaint_id):
    """Delete a pending complaint."""
    complaint = get_object_or_404(Complaint, id=complaint_id, user=request.user)
    if complaint.status != 'PE':
        messages.error(request, "You can't delete a complaint that is already being processed.")
        return redirect('user_dashboard')
    if request.method == 'POST':
        complaint.delete()
        messages.success(request, 'Complaint deleted successfully.')
        return redirect('user_dashboard')
    return render(request, 'complaints/confirm_delete.html', {'complaint': complaint})
def complaint_success(request):
    """Display success page after complaint submission."""
    return render(request, 'complaints/success.html')