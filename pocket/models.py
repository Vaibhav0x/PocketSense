from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.hashers import make_password


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set", 
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set", 
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'): 
            self.password = make_password(self.password) 
        super().save(*args, **kwargs)

class Expense(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='expenses')
    payer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='paid_expenses')
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class Group(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(
        'CustomUser',
        related_name="custom_groups", 
    )

class Balance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='balances')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='balances')
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
