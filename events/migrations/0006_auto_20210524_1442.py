# Generated by Django 3.2.3 on 2021-05-24 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_rename_img_mainbanner_eventimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainbanner',
            old_name='eventName',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='mainbanner',
            old_name='eventimg',
            new_name='maintimg',
        ),
        migrations.RenameField(
            model_name='mainbanner',
            old_name='eventdesc',
            new_name='subheading',
        ),
    ]