"""Initial migration to create the Complaint model."""
from django.db import migrations, models
class Migration(migrations.Migration):
    """Migration class to set up the initial Complaint model."""
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                (
                    'category',
                    models.CharField(
                        choices=[
                            ('FO', 'Food'),
                            ('SV', 'Service'),
                            ('CL', 'Cleanliness')
                        ],
                        max_length=2
                    )
                ),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]