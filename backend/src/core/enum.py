from django.db import models

class DayhomeStatus(models.TextChoices):
    PRESENT = 'present', 'Present'
    ABSENT = 'absent', 'Absent'
    LATE = 'late', 'Late'
    EARLY = 'early', 'Early'
    EXCUSED = 'excused', 'Excused'
    UNEXCUSED = 'unexcused', 'Unexcused'
    INJURED = 'injured', 'Injured'
    SICK = 'sick', 'Sick'