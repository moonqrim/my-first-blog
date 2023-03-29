'''blog 앱 모델 생성'''

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # models. : 장고모델임을 의미
    # 모델 속성
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # 모델 메소드
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title