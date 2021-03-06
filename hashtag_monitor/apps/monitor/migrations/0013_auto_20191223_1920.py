# Generated by Django 3.0 on 2019-12-23 19:20

from django.db import migrations, models
import hashtag_monitor.apps.monitor.models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0012_auto_20191223_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='name',
            field=models.CharField(max_length=500, primary_key=True, serialize=False, validators=[hashtag_monitor.apps.monitor.models.validate_is_hashtag, hashtag_monitor.apps.monitor.models.validate_nb_hashtag, hashtag_monitor.apps.monitor.models.validate_is_not_duplicate, hashtag_monitor.apps.monitor.models.validate_hashtag_not_empty], verbose_name='Hashtag name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers_count',
            field=models.IntegerField(default=0, verbose_name='Followers count'),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends_count',
            field=models.IntegerField(default=0, verbose_name='Friends count'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.URLField(null=True, verbose_name='Profile image url'),
        ),
    ]
