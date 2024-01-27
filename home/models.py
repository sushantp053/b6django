from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_id = models.BigAutoField(primary_key = True)
    image = models.ImageField(upload_to="posts/")
    text = models.TextField()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    posted_at = models.DateTimeField()
    location = models.TextField()

    def __str__(self) -> str:
        return self.text + self.location

class Comments(models.Model):
    comment_id = models.IntegerField(primary_key = True)
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    comment = models.TextField()
    commented_at = models.DateTimeField()

class Like(models.Model):
    like_id = models.IntegerField(primary_key = True)
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    liked_at= models.DateTimeField()

class ComComment(models.Model):
    comId = models.BigAutoField(primary_key = True)
    comment_id = models.ForeignKey(Comments, on_delete = models.CASCADE )
    comment = models.TextField()
    user_id = models.ForeignKey(User, on_delete = models.DO_NOTHING)
