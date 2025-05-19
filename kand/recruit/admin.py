from django.contrib import admin
from .models import Recruit


@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'years_old', 'manager', 'applied_date')
    search_fields = ('name', 'manager')
    list_filter = ('manager', 'applied_date')
    ordering = ('-applied_date',)
    
    def manager_name(self, obj):
        return obj.manager.get_full_name() if obj.manager else "Не назначен"
    
    manager_name.short_description = 'Менеджер'