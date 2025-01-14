from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class UserManger(BaseUserManager):
    def create_user(self, email, name, tc, password = None, password2 = None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(

            email = self.normalize_email(email),
            name = name,
            tc = tc
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, name, tc, password = None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(

            email = email,
            password = password,
            name = name,
            tc = tc
        )

        user.is_admin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        
        verbose_name = "email address",
        max_length = 255,
        unique = True
    )
    
    name = models.CharField(max_length = 300)
    tc = models.BooleanField()
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now_add = True)
    
    objects = UserManger()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "tc"]
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True    
    
    @property
    def is_staff(self):
        return self.is_admin
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "accounts/images", default="accounts/images/default_profile.jpg", null = True, blank = True)
    
    def __str__(self):
        return f"{self.user.name}'s Profile"
    
CHOICES = [
              ("SSC" , "SSC"),
              ("HSC", "HSC"),
              ("Graduation", "Graduation"),
              ("Post Graduation", "Post Graduation")
          ]

class Education(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    degree = models.CharField(max_length=30, choices = CHOICES, default="Graduation")
    specialization = models.CharField(max_length=50)
    institution = models.CharField(max_length = 200)
    board_or_university = models.CharField(max_length=100)
    passing_year = models.DateField()
    
    def __str__(self):
        return f"{self.user.name}'s EDUCATION"
    
    
class Skills(models.Model):
    skill = models.CharField(max_length = 20)
    def __str__(self):
        return self.skill
    

class UserSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.name}'s Skills"

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 60)
    role = models.CharField(max_length = 60, default = "")
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length = 100)
    job_role = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField() 
    experience_year = models.CharField(max_length=50, editable = False)
    
    def save(self, *args, **kwargs):
        if self.start_date and self.end_date:
            duration = self.end_date - self.start_date
            years = duration.days // 365 ; months = (duration.days % 365) // 30
            self.experience_year = f"{years}y {months}m"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.user.name}'s Experience"
       
    
    

