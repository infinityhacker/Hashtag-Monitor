# Generated by Django 3.0 on 2019-12-19 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_auto_20191219_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='is_retweet',
        ),
        migrations.AddField(
            model_name='tweet',
            name='filter_level',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='Twitter filter level'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweeted',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tweet_retweeted', to='monitor.Tweet'),
        ),
        migrations.CreateModel(
            name='QuotedTweet',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Twitter tweet id')),
                ('created_at', models.DateTimeField(verbose_name='Date created')),
                ('lang', models.CharField(max_length=10, verbose_name='Language')),
                ('retweet_count', models.IntegerField(verbose_name='Retweets')),
                ('source', models.CharField(max_length=500, verbose_name='Source')),
                ('text', models.TextField(verbose_name='Text')),
                ('filter_level', models.CharField(default=None, max_length=50, null=True, verbose_name='Twitter filter level')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.User')),
                ('hashtags', models.ManyToManyField(blank=True, to='monitor.Hashtag')),
                ('quoted_tweet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tweet_quoted', to='monitor.QuotedTweet')),
                ('retweeted', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.Tweet')),
            ],
        ),
        migrations.AlterField(
            model_name='tweet',
            name='quoted_tweet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.QuotedTweet'),
        ),
    ]
