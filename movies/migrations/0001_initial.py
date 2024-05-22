# Generated by Django 5.0.6 on 2024-05-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Actor')),
            ],
        ),
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='DirectorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Director')),
            ],
        ),
        migrations.CreateModel(
            name='LanguageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Language')),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100, verbose_name='Genre')),
            ],
        ),
        migrations.CreateModel(
            name='WriterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Writer')),
            ],
        ),
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('rated', models.CharField(choices=[('N/A', 'NOT_AVAILABLE'), ('Unrated', 'UNRATED'), ('R', 'R_RATED'), ('PG-13', 'PG_13'), ('Not Rated', 'NOT_RATED'), ('TV-14', 'TV_14'), ('PG', 'PG')], default='N/A', max_length=12)),
                ('released', models.DateField(verbose_name='Release Date')),
                ('runtime', models.IntegerField(verbose_name='Runtime')),
                ('plot', models.TextField(verbose_name='Plot')),
                ('awards', models.TextField(verbose_name='Awards')),
                ('poster', models.URLField(verbose_name='Poster')),
                ('meta_score', models.CharField(max_length=16, verbose_name='Meta Score')),
                ('imdb_rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='IMDB Rating')),
                ('imdb_votes', models.BigIntegerField(verbose_name='IMDB Votes')),
                ('imdb_id', models.CharField(max_length=16, verbose_name='IMDB Id')),
                ('type', models.CharField(max_length=16, verbose_name='Type')),
                ('dvd', models.DateField(null=True, verbose_name='DVD Release Date')),
                ('box_office', models.BigIntegerField(verbose_name='Box Office')),
                ('production', models.CharField(max_length=128, verbose_name='Production')),
                ('website', models.URLField(verbose_name='Website')),
                ('ratings', models.JSONField()),
                ('date', models.DateTimeField(null=True, verbose_name='Date')),
                ('actors', models.ManyToManyField(to='movies.actormodel')),
                ('country', models.ManyToManyField(to='movies.countrymodel')),
                ('director', models.ManyToManyField(to='movies.directormodel')),
                ('genre', models.ManyToManyField(to='movies.moviegenre')),
                ('language', models.ManyToManyField(to='movies.languagemodel')),
                ('writer', models.ManyToManyField(to='movies.writermodel')),
            ],
        ),
    ]
