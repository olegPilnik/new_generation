from django.db import models


class Profile(models.Model):
        user_id = models.PositiveIntegerField(unique=True, 
                                              verbose_name='user ID telegram')
        user_name = models.CharField(max_length=30, blank=True, null=True,
                                        verbose_name='user_name telegram')
        
        full_name = models.CharField(max_length=70, blank=True, null=True,
                                      verbose_name="Повне ім'я" )
        
        def __str__(self):
            return f'{self.user_id}'


        class Meta:
            verbose_name = 'Профіль'
            verbose_name_plural = 'Профілі'
            ordering = ('id', )
