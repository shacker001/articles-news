"""
WSGI config for chronicles project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chronicles.settings')

application = get_wsgi_application()

app = application

import cloudinary
from dotenv import load_dotenv
load_dotenv()

cloudinary.config(cloud_name= os.environ.get("CLOUDINARY_CLOUD_NAME"),
                  api_key=os.environ.get("CLOUDINARY_API_KEY"),
                  api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
                  secure = True)