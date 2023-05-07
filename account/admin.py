from django.contrib import admin
from .models import Account, WorkHistory
from .forms import AccountChangeForm, AccountFormsCreate

admin.site.register(WorkHistory)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    add_form = AccountFormsCreate
    list_display = ['id', 'email', 'first_name', 'last_name', 'image', 'role', 'is_superuser',
                    'is_active', 'is_staff', 'date_created', 'date_modified', ]
    search_fields = ['email', 'firs_name', 'last_name']
    list_filter = ['role', 'is_superuser', 'is_active', 'is_staff', 'date_created']
    date_hierarchy = 'date_created'
    list_display_links = ['id', 'email']



