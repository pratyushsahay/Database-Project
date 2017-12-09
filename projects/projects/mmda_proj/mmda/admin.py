from django.contrib import admin

from .models import Question, Choice, File, Creation_Metadata, Document
from .models import Image, Webpage

# Register your models here.

#admin.site.register(Question)

#admin.site.register(Choice)

admin.site.register(File)
admin.site.register(Creation_Metadata)
admin.site.register(Document)
admin.site.register(Image)
admin.site.register(Webpage)
