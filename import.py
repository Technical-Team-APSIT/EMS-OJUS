import csv
import sys
import os
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.hashers import make_password

project_dir = "/EMS/core/"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'EMS.settings'
import django
django.setup()

User = get_user_model()

file = 'data.csv'

data = csv.reader(open(file), delimiter=",")
for row in data:
    pwd = row[1]+row[2]
    print(f"Username: {row[1]}, Password: {pwd}")

    # Use get_or_create to avoid creating duplicate users
    user, created = User.objects.get_or_create(
        username=row[1],
        defaults={
            'password': make_password(pwd),
            'last_login': timezone.now(),
            'is_superuser': False,
            'fname': row[2],
            'lname': row[4],
            'is_staff': True,
            'is_active': True,
            'date_joined': timezone.now(),
            'dept': row[5],
            'year': row[6],
            'moodle_id': row[1],
        }
    )

    if not created:
        # User already existed, update fields
        user.set_password(pwd)  # Use set_password method
        user.last_login = timezone.now()
        user.fname = row[1]
        user.lname = row[2]
        user.dept = row[4]
        user.year = row[5]
        user.moodle_id = row[0]
        user.save()
