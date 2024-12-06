from django.db import models
from django.utils.text import slugify

# Model Field
class Field(models.Model):
    field_name = models.CharField(max_length=100)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.TextField()
    field_image = models.ImageField(upload_to='field/', blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField(blank=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.field_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.field_name

# Model Schedule
class Schedule(models.Model):
    SCHEDULE_STATUS = [
        ('Available', 'Available'),
        ('Booked', 'Booked'),
    ]
    
    SESSION_CHOICES = [
        ('session1', '08:00 - 10:00'),
        ('session2', '10:00 - 12:00'),
        ('session3', '12:00 - 14:00'),
        ('session4', '14:00 - 16:00'),
        ('session5', '16:00 - 18:00'),
        ('session6', '18:00 - 20:00'),
        ('session7', '20:00 - 22:00'),
    ]

    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    session = models.CharField(max_length=20, choices=SESSION_CHOICES)
    status = models.CharField(max_length=10, choices=SCHEDULE_STATUS, default='Available')

    class Meta:
        unique_together = ('field', 'date', 'session')
        ordering = ['date', 'session']

    def __str__(self):
        return f"{self.field.field_name} - {self.date} - {self.session}"
