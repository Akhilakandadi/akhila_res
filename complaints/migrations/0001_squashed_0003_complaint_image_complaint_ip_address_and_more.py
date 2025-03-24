"""Squashed migration for complaints app up to 0003, creating Complaint and StatusHistory models."""
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ('complaints', '0001_initial'),
        ('complaints', '0002_complaint_email_complaint_status'),
        ('complaints', '0003_complaint_image_complaint_ip_address_and_more'),
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('FO', 'Food'), ('SV', 'Service'), ('CL', 'Cleanliness')], max_length=2)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(choices=[('PE', 'Pending'), ('RE', 'Resolved'), ('IP', 'In Progress')], default='PE', max_length=2)),
                ('image', models.ImageField(blank=True, null=True, upload_to='complaints/')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('is_urgent', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('priority', models.CharField(choices=[('HI', 'High'), ('ME', 'Medium'), ('LO', 'Low')], default='ME', max_length=2)),
                ('resolution', models.TextField(blank=True, null=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('resolved_by', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='resolved_complaints',
                    to=settings.AUTH_USER_MODEL
                )),
                ('status_updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL
                )),
            ],
        ),
        migrations.CreateModel(
            name='StatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_status', models.CharField(choices=[('PE', 'Pending'), ('RE', 'Resolved'), ('IP', 'In Progress')], max_length=2)),
                ('new_status', models.CharField(choices=[('PE', 'Pending'), ('RE', 'Resolved'), ('IP', 'In Progress')], max_length=2)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.complaint')),
            ],
        ),
    ]