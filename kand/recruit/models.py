from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Recruit(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')
    years_old = models.PositiveIntegerField()
    manager = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,  # или models.PROTECT, если нельзя удалять менеджера с клиентами
        null=True,
        blank=True,
        related_name='clients'  # позволяет обращаться user.clients.all()
    )
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Recruit'
        verbose_name_plural = 'Recruits'
        ordering = ['-applied_date']
    
    @property
    def manager_name(self):
        return self.manager.get_full_name() if self.manager else "Не назначен"
    
   