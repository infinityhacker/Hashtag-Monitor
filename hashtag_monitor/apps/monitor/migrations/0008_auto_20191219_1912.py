# Generated by Django 3.0 on 2019-12-19 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_auto_20191219_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='quoted_tweet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tweet_quoted', to='monitor.Tweet'),
        ),
        migrations.DeleteModel(
            name='QuotedTweet',
        ),
    ]
