from django.db import models
from django.urls import reverse

# Create your models here.
class table_topic(models.Model):
    col_topic1 = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.col_topic1

    def get_absolute_url(self):
        '''
        this function is used if we want
        to do CRUD action with the table
        '''
        return reverse('test_app:create')


class table_webpage(models.Model):
    col_webpage1 = models.ForeignKey(table_topic, on_delete=models.CASCADE)
    col_webpage2 = models.CharField(max_length=264, unique=True)
    col_webpage3 = models.URLField(unique=True)

    def __str__(self):
        return self.col_webpage2


class table_AccessRecord(models.Model):
    col_AccessRecord1 = models.ForeignKey(table_webpage, related_name='accrec', on_delete=models.CASCADE)
    col_AccessRecord2 = models.DateField()

    def __str__(self):
        return str(self.col_AccessRecord2)


# ======================= MODELS FOR FORMS ======================================

class table_User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    emailadd = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.username


# ======================= MODELS FOR USERPROFILE ======================================
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username