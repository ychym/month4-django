from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField()

class Tag(models.Model):
    name = models.CharField()

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField()
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(null=True, upload_to="posts")#upload_to="posts" -medianyn ichinde posts foulder tuzot





# #CRUD - C -->django do koldo tuzunun keregi jok django ozu automatically kylat

# #Create
# #INSERT INTO table_name (title, text) VALUES (?, ?);

# #way 1
# post_1 = Post(title="title", text="text")
# post_1.save()

# #way2
# post_2 = Post.objects.create(title="title_2", text="text_2")


# #Read - R
# #SELECT * FROM table_name WHERE title IN ('value')
# posts = Post.objects.all()

# #Update - U
# #UPDATE table_name SET title = "title" WHERE id = 1;
# post_1.title = "title edited"
# post_1.save()

# #Delete - D
# #DELETE FROM table_name WHERE id = 1;
# post_1.delete()
