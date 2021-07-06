from django.db import models

# Create your models here.



#모델은 클래스를 사용합니다.
# models 안에 있는 M을 상속받아와서 코드를 만들것이다.
# migrate를 배움
# python manage.py makemigrations -> 장고와 models을 연결
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)