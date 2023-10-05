from django.db import models
from django.contrib.auth.models import User


class BasicNote(models.Model):
    name = models.CharField("Title", max_length=32)
    desc = models.CharField("Description", max_length=50, null=True, blank=True)
    checkmark = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=7, default="#f39c12")
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    until = models.DateTimeField("Date", null=True, blank=True)

    def __str__(self):
        return self.name


class ScheduleBlock(models.Model):
    class Weekday(models.TextChoices):
        mon = "Monday", "Monday"
        tue = "Tuesday", "Tuesday"
        wed = "Wednesday", "Wednesday"
        thu = "Thursday", "Thursday"
        fri = "Friday", "Friday"
        sat = "Saturday", "Saturday"
        sun = "Sunday", "Sunday"
    name = models.CharField(max_length=32)
    day = models.CharField(max_length=10, choices=Weekday.choices)
    startTime = models.TimeField("Start Time")
    endTime = models.TimeField("End Time", null=True, blank=True)
    startTimeWhenLastEnds = models.BooleanField(default=False)
    endTimeWhenNextBegins = models.BooleanField(default=False)
    color = models.CharField(max_length=7, default="#f39c12")
    user = models.ForeignKey(User, on_delete=models.CASCADE)