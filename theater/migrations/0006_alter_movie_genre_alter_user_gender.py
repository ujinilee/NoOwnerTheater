# Generated by Django 4.0.1 on 2022-02-08 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0005_auto_20220208_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('공포(호러)', '공포(호러)'), ('가족', '가족'), ('애니메이션', '애니메이션'), ('다큐멘터리', '다큐멘터리'), ('범죄', '범죄'), ('스릴러', '스릴러'), ('미스터리', '미스터리'), ('드라마', '드라마'), ('전쟁', '전쟁'), ('액션', '액션'), ('판타지', '판타지'), ('뮤지컬', '뮤지컬'), ('SF', 'SF'), ('코미디', '코미디'), ('멜로/로맨스', '멜로/로맨스'), ('사극', '사극'), ('성인물(에로)', '성인물(에로)')], max_length=100, verbose_name='장르'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('남자', '남자'), ('여자', '여자')], max_length=20, verbose_name='성별'),
        ),
    ]
