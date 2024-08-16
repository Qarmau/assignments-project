from django.db import models

# Create your models here.
from django.db import models

grades=[
    (1,1),
    (2,2),
    (3,3),
    (4,4)
]


subjects=[
    ('MATHEMATICS','MATHEMATICS'),
    ('ENGLISH','ENGLISH'),
    ('KISWAHILI','KISWAHILI'),
    ('CHEMISTRY','CHEMISTRY'),
    ('PHYSICS','PHYSICS'),
    ('BIOLOGY','BIOLOGY'),
    ('BUSINESS STUDIES','BUSINESS STUDIES'),
    ('COMPUTER STUDIES','COMPUTER STUDIES'),
    ('AGRICULTURE','AGRICULTURE'),
    ('HOME SCIENCE','HOME SCIENCE'),
    ('HISTORY','HISTORY'),
    ('GEOGRAPHY','GEOGRAPHY'),
    ('CRE','CRE')
]

class Assignment(models.Model):
    title = models.CharField(max_length=200, default='AUGUST HOLIDAY ASSIGNMENT')
    grade=models.IntegerField(choices=grades)
    subject=models.CharField(max_length=50,choices=subjects)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='assignments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title