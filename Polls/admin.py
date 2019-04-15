from django.contrib import admin
from Polls.models import *


admin.site.register(Question)
admin.site.register(Choice)
