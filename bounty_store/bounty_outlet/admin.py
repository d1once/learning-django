from django.contrib import admin
from .models import Bounty

# Register your models here.


class BountyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("benefactor", "reward",)
    list_display = ("name", "benefactor",)


admin.site.register(Bounty, BountyAdmin)
