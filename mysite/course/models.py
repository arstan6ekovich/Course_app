from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('admin', 'admin'),
    )
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='student')
    profile_picture = models.ImageField(upload_to='user_profile', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.role}'


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.subcategory_name


class Course(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    LEVEL_CHOICES = (
        ('beginner', 'beginner'),
        ('intermediate', 'intermediate'),
        ('advanced', 'advanced'),
    )
    level = models.CharField(max_length=16, choices=LEVEL_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.course_name}, {self.level}'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=100)
    video_url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return f'{self.course}, {self.lesson_title}'


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    students = models.ManyToManyField(UserProfile, blank=True,)


    def __str__(self):
        return f'{self.course}, {self.assignment_title}'


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_title = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return f'{self.course}, {self.exam_title}'


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.exam}, {self.question_name}'


class Option(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_name = models.CharField(max_length=150)
    type_option = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.questions}, {self.option_name}'


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField()
    certificate_url = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f'{self.course}, {self.student}'


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])


    def __str__(self):
        return f'{self.course}, {self.user}, {self.rating}'

