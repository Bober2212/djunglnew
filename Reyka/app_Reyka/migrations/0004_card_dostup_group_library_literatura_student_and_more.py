# Generated by Django 4.2.6 on 2023-11-10 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_Reyka', '0003_alter_project_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='card_dostup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issue', models.DateField()),
                ('close_date', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studens_group', models.CharField(max_length=30)),
                ('group_number', models.CharField(max_length=30)),
                ('cabinete_fences', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='library_literatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ganr', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('date_publication', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('number_studens_card', models.IntegerField()),
                ('gmail', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='proces_taking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_literature', models.CharField(max_length=30)),
                ('number_studens_card', models.IntegerField()),
                ('date_issue', models.DateField()),
                ('name_surname', models.DateField()),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Reyka.library_literatura')),
                ('library_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Reyka.card_dostup')),
            ],
        ),
        migrations.AddField(
            model_name='card_dostup',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Reyka.student'),
        ),
    ]