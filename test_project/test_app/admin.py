from django.contrib import admin
from test_app.models import table_topic, table_webpage, table_AccessRecord, table_User, UserProfileInfo

# Register your models here.
admin.site.register(table_topic)
admin.site.register(table_webpage)
admin.site.register(table_AccessRecord)
admin.site.register(table_User)
admin.site.register(UserProfileInfo)