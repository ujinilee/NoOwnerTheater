# Generated by Django 4.0.2 on 2022-02-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0003_alter_releasedmovie_genre_alter_releasedmovie_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releasedmovie',
            name='genre',
            field=models.CharField(choices=[('스릴러', '스릴러'), ('SF', 'SF'), ('성인물(에로)', '성인물(에로)'), ('다큐멘터리', '다큐멘터리'), ('범죄', '범죄'), ('애니메이션', '애니메이션'), ('코미디', '코미디'), ('사극', '사극'), ('드라마', '드라마'), ('가족', '가족'), ('미스터리', '미스터리'), ('액션', '액션'), ('전쟁', '전쟁'), ('뮤지컬', '뮤지컬'), ('판타지', '판타지'), ('멜로/로맨스', '멜로/로맨스'), ('공포(호러)', '공포(호러)')], max_length=100, verbose_name='장르'),
        ),
        migrations.AlterField(
            model_name='releasedmovie',
            name='grade',
            field=models.CharField(choices=[('청소년 관람불가', '청소년 관람불가'), ('15세', '15세'), ('12세', '12세'), ('전체 관람가', '전체 관람가')], max_length=20, verbose_name='등급'),
        ),
        migrations.AlterField(
            model_name='unreleasedmovie',
            name='genre',
            field=models.CharField(choices=[('스릴러', '스릴러'), ('SF', 'SF'), ('성인물(에로)', '성인물(에로)'), ('다큐멘터리', '다큐멘터리'), ('범죄', '범죄'), ('애니메이션', '애니메이션'), ('코미디', '코미디'), ('사극', '사극'), ('드라마', '드라마'), ('가족', '가족'), ('미스터리', '미스터리'), ('액션', '액션'), ('전쟁', '전쟁'), ('뮤지컬', '뮤지컬'), ('판타지', '판타지'), ('멜로/로맨스', '멜로/로맨스'), ('공포(호러)', '공포(호러)')], max_length=100, verbose_name='장르'),
        ),
        migrations.AlterField(
            model_name='unreleasedmovie',
            name='grade',
            field=models.CharField(blank=True, choices=[('청소년 관람불가', '청소년 관람불가'), ('15세', '15세'), ('12세', '12세'), ('전체 관람가', '전체 관람가')], max_length=20, null=True, verbose_name='등급'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('일반 사용자', '일반 사용자'), ('제작사', '제작사')], max_length=20, verbose_name='가입 유형'),
        ),
    ]
