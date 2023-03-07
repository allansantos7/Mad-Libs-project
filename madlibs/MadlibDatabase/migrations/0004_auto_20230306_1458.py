# Generated by Django 2.2 on 2023-03-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MadlibDatabase', '0003_baseball_blindmice_catfiddle_fortune_greetings_industryaward_katie_newday_pizza_sicknote_tolkien_val'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adjective_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Animal_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalPlural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AnimalPlural_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BodyPart_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clothing_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Color_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fruit_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Illness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Illness_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instrument_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Noun_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NounPlural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NounPlural_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_name', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Relation_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Verb_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Word_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Baseball',
        ),
        migrations.DeleteModel(
            name='BeKind',
        ),
        migrations.DeleteModel(
            name='BlindMice',
        ),
        migrations.DeleteModel(
            name='CatFiddle',
        ),
        migrations.DeleteModel(
            name='Fortune',
        ),
        migrations.DeleteModel(
            name='Greetings',
        ),
        migrations.DeleteModel(
            name='IndustryAward',
        ),
        migrations.DeleteModel(
            name='Katie',
        ),
        migrations.DeleteModel(
            name='NewDay',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='SickNote',
        ),
        migrations.DeleteModel(
            name='Tolkien',
        ),
        migrations.DeleteModel(
            name='Valentine',
        ),
        migrations.DeleteModel(
            name='VideoGame',
        ),
        migrations.DeleteModel(
            name='Yankee',
        ),
    ]
