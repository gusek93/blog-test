from django.db import models


class User():
    email = models.EmailField('이메일', max_length=255, unique=True)
    name = models.CharField('이름', max_length=100)
    is_staff = models.BooleanField('직원 유무', default=False)
    is_activate = models.BooleanField('활성 여부', default=False)
    
    class Meta:
        db_table = 'users'
        ordering = ['-id']
        
        