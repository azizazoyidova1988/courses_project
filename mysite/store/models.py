from django.db import models


class Items(models.Model):
    title = models.CharField(max_length=120, blank=False, null=True)
    image = models.FileField(upload_to='image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "items"


class Course(models.Model):
    title = models.CharField(max_length=120, blank=False, null=True)
    image = models.ImageField(upload_to='image/', blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "course"


class Team(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    degree = models.CharField(max_length=150, blank=False, null=True)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "team"


class Subscribe(models.Model):
    email = models.EmailField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "subscribe"


class News(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "news"


class Video(models.Model):
    title = models.CharField(max_length=120, blank=False, null=True)
    video = models.FileField(upload_to='video/', blank=False, null=False)
    description = models.TextField(blank=False, null=True)
    course = models.ForeignKey(Course, blank=False, null=True, on_delete=models.SET_NULL)
    count = models.PositiveIntegerField(default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "video"


class Commenter(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(max_length=350, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    video = models.ForeignKey(Video, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "commenter"
