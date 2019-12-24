# Generated by Django 3.0 on 2019-12-19 15:06

from django.db import migrations, models
import django.db.models.deletion
import hashtag_monitor.apps.monitor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('name', models.CharField(max_length=500, primary_key=True, serialize=False, validators=[hashtag_monitor.apps.monitor.models.validate_is_hashtag], verbose_name='Hashtag name')),
                ('color', models.CharField(choices=[('red darken-1', 'red-1'), ('red darken-2', 'red-2'), ('red darken-3', 'red-3'), ('red darken-4', 'red-4'), ('pink darken-1', 'pink-1'), ('pink darken-2', 'pink-2'), ('pink darken-3', 'pink-3'), ('pink darken-4', 'pink-4'), ('purple darken-1', 'purple-1'), ('purple darken-2', 'purple-2'), ('purple darken-3', 'purple-3'), ('purple darken-4', 'purple-4'), ('deep-purple darken-1', 'deep-purple-1'), ('deep-purple darken-2', 'deep-purple-2'), ('deep-purple darken-3', 'deep-purple-3'), ('deep-purple darken-4', 'deep-purple-4'), ('indigo darken-1', 'indigo-1'), ('indigo darken-2', 'indigo-2'), ('indigo darken-3', 'indigo-3'), ('indigo darken-4', 'indigo-4'), ('blue darken-1', 'blue-1'), ('blue darken-2', 'blue-2'), ('blue darken-3', 'blue-3'), ('blue darken-4', 'blue-4'), ('light-blue darken-1', 'light-blue-1'), ('light-blue darken-2', 'light-blue-2'), ('light-blue darken-3', 'light-blue-3'), ('light-blue darken-4', 'light-blue-4'), ('cyan darken-1', 'cyan-1'), ('cyan darken-2', 'cyan-2'), ('cyan darken-3', 'cyan-3'), ('cyan darken-4', 'cyan-4'), ('teal darken-1', 'teal-1'), ('teal darken-2', 'teal-2'), ('teal darken-3', 'teal-3'), ('teal darken-4', 'teal-4'), ('green darken-1', 'green-1'), ('green darken-2', 'green-2'), ('green darken-3', 'green-3'), ('green darken-4', 'green-4'), ('light-green darken-1', 'light-green-1'), ('light-green darken-2', 'light-green-2'), ('light-green darken-3', 'light-green-3'), ('light-green darken-4', 'light-green-4'), ('lime darken-1', 'lime-1'), ('lime darken-2', 'lime-2'), ('lime darken-3', 'lime-3'), ('lime darken-4', 'lime-4'), ('yellow darken-1', 'yellow-1'), ('yellow darken-2', 'yellow-2'), ('yellow darken-3', 'yellow-3'), ('yellow darken-4', 'yellow-4'), ('amber darken-1', 'amber-1'), ('amber darken-2', 'amber-2'), ('amber darken-3', 'amber-3'), ('amber darken-4', 'amber-4'), ('orange darken-1', 'orange-1'), ('orange darken-2', 'orange-2'), ('orange darken-3', 'orange-3'), ('orange darken-4', 'orange-4'), ('deep-orange darken-1', 'deep-orange-1'), ('deep-orange darken-2', 'deep-orange-2'), ('deep-orange darken-3', 'deep-orange-3'), ('deep-orange darken-4', 'deep-orange-4'), ('brown darken-1', 'brown-1'), ('brown darken-2', 'brown-2'), ('brown darken-3', 'brown-3'), ('brown darken-4', 'brown-4'), ('grey darken-1', 'grey-1'), ('grey darken-2', 'grey-2'), ('grey darken-3', 'grey-3'), ('grey darken-4', 'grey-4'), ('blue-grey darken-1', 'blue-grey-1'), ('blue-grey darken-2', 'blue-grey-2'), ('blue-grey darken-3', 'blue-grey-3'), ('blue-grey darken-4', 'blue-grey-4'), ('mdb-color darken-1', 'mdb-color-1'), ('mdb-color darken-2', 'mdb-color-2'), ('mdb-color darken-3', 'mdb-color-3'), ('mdb-color darken-4', 'mdb-color-4')], default=None, max_length=50, null=True, verbose_name='Color class')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Twitter user id')),
                ('name', models.CharField(max_length=100, verbose_name='Username')),
                ('screen_name', models.CharField(max_length=100, verbose_name='Username')),
                ('location', models.CharField(max_length=500, verbose_name='Location')),
                ('friends_count', models.IntegerField(verbose_name='Friends count')),
                ('followers_count', models.IntegerField(verbose_name='Followers count')),
                ('created_at', models.DateField(verbose_name='Date created')),
                ('profile_image', models.URLField(verbose_name='Profile image url')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Twitter tweet id')),
                ('created_at', models.DateTimeField(verbose_name='Date created')),
                ('lang', models.CharField(max_length=10, verbose_name='Language')),
                ('retweet_count', models.IntegerField(verbose_name='Retweets')),
                ('source', models.CharField(max_length=500, verbose_name='Source')),
                ('text', models.TextField(verbose_name='Text')),
                ('is_retweet', models.BooleanField(default=False, verbose_name='Is retweet')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.User')),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Hashtag')),
            ],
        ),
    ]
