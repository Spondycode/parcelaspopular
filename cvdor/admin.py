from django.contrib import admin

from .models import Campsite
from .models import User
from .models import Parcela
from .models import Sun
from .models import Group

admin.site.register(Campsite)
admin.site.register(User)
admin.site.register(Parcela)
admin.site.register(Sun)
admin.site.register(Group)


