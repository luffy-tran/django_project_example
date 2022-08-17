# Generated by Django 4.1 on 2022-08-17 06:36

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('name', models.CharField(default=None, max_length=255, null=True)),
                ('total', models.IntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name': 'Example',
                'verbose_name_plural': 'Examples',
                'db_table': 'example',
            },
        ),
        migrations.AddIndex(
            model_name='example',
            index=models.Index(fields=['-id', '-name'], name='example_id_920004_idx'),
        ),
    ]