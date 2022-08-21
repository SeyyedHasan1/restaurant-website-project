# Generated by Django 4.1 on 2022-08-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=50, verbose_name='توضیحات')),
                ('rate', models.IntegerField(default=0, verbose_name='امتیاز')),
                ('price', models.IntegerField()),
                ('time', models.IntegerField(verbose_name='زمان لازم')),
                ('pub_time', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('photo', models.ImageField(upload_to='foods/')),
                ('type_food', models.CharField(choices=[('breakfast', 'صبحانه'), ('drinks', 'نوشیدنی'), ('lunch', 'نهار'), ('dinner', 'شام')], default='drinks', max_length=10, verbose_name='نوع غذا')),
            ],
        ),
    ]
