from django.db import models


# Create your models here.
class Member(models.Model):
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)

    contact     = models.CharField(max_length=20)
   
   # SELF-REFERENTIAL FOREIGN KEY FOR INVITER
    invited_by  = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='referrals',
        help_text='The existing member who invited this person (optional)',
    )

    location    = models.CharField(max_length=255)
    date_joined = models.DateField()
    created_at  = models.DateTimeField(auto_now_add=True)


     # MODEL META
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'