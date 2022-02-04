# Generated by Django 4.0.1 on 2022-02-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unreleasedmovie',
            name='intro_detail',
        ),
        migrations.AlterField(
            model_name='releasedmovie',
            name='genre',
            field=models.CharField(choices=[('범죄', '범죄'), ('애니메이션', '애니메이션'), ('스릴러', '스릴러'), ('미스터리', '미스터리'), ('뮤지컬', '뮤지컬'), ('사극', '사극'), ('전쟁', '전쟁'), ('액션', '액션'), ('판타지', '판타지'), ('코미디', '코미디'), ('SF', 'SF'), ('드라마', '드라마'), ('성인물(에로)', '성인물(에로)'), ('다큐멘터리', '다큐멘터리'), ('멜로/로맨스', '멜로/로맨스'), ('공포(호러)', '공포(호러)'), ('가족', '가족')], max_length=100, verbose_name='장르'),
        ),
        migrations.AlterField(
            model_name='releasedmovie',
            name='grade',
            field=models.CharField(choices=[('전체 관람가', '전체 관람가'), ('15세', '15세'), ('청소년 관람불가', '청소년 관람불가'), ('12세', '12세')], max_length=20, verbose_name='등급'),
        ),
        migrations.AlterField(
            model_name='releasedmovie',
            name='release',
            field=models.DateField(verbose_name='개봉'),
        ),
        migrations.AlterField(
            model_name='releasedmovie',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='예고편'),
        ),
        migrations.AlterField(
            model_name='unreleasedmovie',
            name='actor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='출연'),
        ),
        migrations.AlterField(
            model_name='unreleasedmovie',
            name='director',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='감독'),
        ),
        migrations.AlterField(
            model_name='unreleasedmovie',
            name='genre',
            field=models.CharField(choices=[('범죄', '범죄'), ('애니메이션', '애니메이션'), ('스릴러', '스릴러'), ('미스터리', '미스터리'), ('뮤지컬', '뮤지컬'), ('사극', '사극'), ('전쟁', '전쟁'), ('액션', '액션'), ('판타지', '판타지'), ('코미디', '코미디'), ('SF', 'SF'), ('드라마', '드라마'), ('성인물(에로)', '성인물(에로)'), ('다큐멘터리', '다큐멘터리'), ('멜로/로맨스', '멜로/로맨스'), ('공포(호러)', '공포(호러)'), ('가족', '가족')], max_length=100, verbose_name='장르'),
        ),
        migrations.AlterField(
            model_name='unreleasedmovie',
            name='gift',
            field=models.TextField(verbose_name='선물 설명'),
        ),
        migrations.AlterField(
            model_name='unreleasedmovie',
            name='grade',
            field=models.CharField(blank=True, choices=[('전체 관람가', '전체 관람가'), ('15세', '15세'), ('청소년 관람불가', '청소년 관람불가'), ('12세', '12세')], max_length=20, null=True, verbose_name='등급'),
        ),
        migrations.AlterField(
            model_name='unreleasedmovie',
            name='intro',
            field=models.TextField(verbose_name='소개'),
        ),
        migrations.AlterField(
            model_name='unreleasedmovie',
            name='money',
            field=models.IntegerField(default=0, verbose_name='펀딩 금액'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('제작사', '제작사'), ('일반 사용자', '일반 사용자')], max_length=20, verbose_name='가입 유형'),
        ),
    ]
