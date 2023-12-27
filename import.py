import csv
import sys
import os
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

project_dir = "/EMS/core/"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'EMS.settings'
import django
django.setup()

User = get_user_model()

file = 'RandomData.csv'

data = csv.reader(open(file), delimiter=",")
for row in data:
    # Use get_or_create to avoid creating duplicate users
    user, created = User.objects.get_or_create(
        username=row[0],
        defaults={
            'password': row[3],
            'last_login': timezone.now(),
            'is_superuser': False,
            'fname': row[1],
            'last_name': row[2],
            'is_staff': True,
            'is_active': True,
            'date_joined': timezone.now(),
            'dept': row[4],
            'year': row[5],
            'moodle_id': row[0],
        }
    )

    if not created:
        # User already existed, update fields
        user.password = row[3]
        user.last_login = timezone.now()
        user.fname = row[1]
        user.lname = row[2]
        user.dept = row[4]
        user.year = row[5]
        user.moodle_id = row[0]
        user.save()
