from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=100)
    contrnt = models.TextField()
    photo = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

        

class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()


