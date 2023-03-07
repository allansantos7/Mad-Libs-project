from django.db import models


# Create your models here.
class BeKind(models.Model):

    BeKind_noun1 = models.CharField(max_length=200)
    BeKind_noun2 = models.CharField(max_length=200)
    BeKind_noun3 = models.CharField(max_length=200)
    BeKind_noun_plural1 = models.CharField(max_length=200)
    BeKind_adj1 = models.CharField(max_length=200)
    BeKind_adj2 = models.CharField(max_length=200)
    BeKind_place1 = models.CharField(max_length=200)


class SickNote(models.Model):
    SickNote_word1 = models.CharField(max_length=200)
    SickNote_word2 = models.CharField(max_length=200)
    SickNote_name1 = models.CharField(max_length=200)
    SickNote_illness1 = models.CharField(max_length=200)
    SickNote_noun_plural1 = models.CharField(max_length=200)
    SickNote_adj1 = models.CharField(max_length=200)
    SickNote_adj2 = models.CharField(max_length=200)


class Greetings(models.Model):
    Greetings_noun_plural1 = models.CharField(max_length=200)
    Greetings_occupation1 = models.CharField(max_length=200)
    Greetings_animal_plural1 = models.CharField(max_length=200)
    Greetings_adj1 = models.CharField(max_length=200)
    Greetings_place1 = models.CharField(max_length=200)
    Greetings_verb1 = models.CharField(max_length=200)
    Greetings_noun1 = models.CharField(max_length=200)


class CatFiddle(models.Model):
    CatFiddle_word1 = models.CharField(max_length=200)
    CatFiddle_animal1 = models.CharField(max_length=200)
    CatFiddle_instrument1 = models.CharField(max_length=200)
    CatFiddle_adj1 = models.CharField(max_length=200)
    CatFiddle_adj2 = models.CharField(max_length=200)
    CatFiddle_noun1 = models.CharField(max_length=200)
    CatFiddle_noun2 = models.CharField(max_length=200)


class Katie(models.Model):
    Katie_verb1 = models.CharField(max_length=200)
    Katie_verb2 = models.CharField(max_length=200)
    Katie_verb3 = models.CharField(max_length=200)
    Katie_noun1 = models.CharField(max_length=200)
    Katie_part1 = models.CharField(max_length=200)
    Katie_animal1 = models.CharField(max_length=200)
    Katie_adj1 = models.CharField(max_length=200)


class NewDay(models.Model):
    NewDay_verb1 = models.CharField(max_length=200)
    NewDay_verb2 = models.CharField(max_length=200)
    NewDay_verb3 = models.CharField(max_length=200)
    NewDay_verb4 = models.CharField(max_length=200)
    NewDay_verb5 = models.CharField(max_length=200)
    NewDay_place1 = models.CharField(max_length=200)
    NewDay_adj1 = models.CharField(max_length=200)


class IndustryAward(models.Model):
    IndustryAward_company1 = models.CharField(max_length=200)
    IndustryAward_noun1 = models.CharField(max_length=200)
    IndustryAward_noun2 = models.CharField(max_length=200)
    IndustryAward_noun3 = models.CharField(max_length=200)
    IndustryAward_noun4 = models.CharField(max_length=200)
    IndustryAward_adj1 = models.CharField(max_length=200)
    IndustryAward_adj2 = models.CharField(max_length=200)


class Tolkien(models.Model):
    Tolkien_fruit1 = models.CharField(max_length=200)
    Tolkien_noun1 = models.CharField(max_length=200)
    Tolkien_noun2 = models.CharField(max_length=200)
    Tolkien_noun3 = models.CharField(max_length=200)
    Tolkien_noun4 = models.CharField(max_length=200)
    Tolkien_noun5 = models.CharField(max_length=200)
    Tolkien_word1 = models.CharField(max_length=200)


class BlindMice(models.Model):
    BlindMice_number1 = models.IntegerField()
    BlindMice_adj1 = models.CharField(max_length=200)
    BlindMice_verb1 = models.CharField(max_length=200)
    BlindMice_job1 = models.CharField(max_length=200)
    BlindMice_relation1 = models.CharField(max_length=200)
    BlindMice_part1 = models.CharField(max_length=200)
    BlindMice_noun1 = models.CharField(max_length=200)


class Valentine(models.Model):
    Valentine_noun1 = models.CharField(max_length=200)
    Valentine_noun2 = models.CharField(max_length=200)
    Valentine_noun3 = models.CharField(max_length=200)
    Valentine_adj1 = models.CharField(max_length=200)
    Valentine_verb1 = models.CharField(max_length=200)
    Valentine_color1 = models.CharField(max_length=200)
    Valentine_part1 = models.CharField(max_length=200)


class Yankee(models.Model):
    Yankee_noun1 = models.CharField(max_length=200)
    Yankee_noun2 = models.CharField(max_length=200)
    Yankee_noun3 = models.CharField(max_length=200)
    Yankee_noun4 = models.CharField(max_length=200)
    Yankee_verb1 = models.CharField(max_length=200)
    Yankee_animal1 = models.CharField(max_length=200)
    Yankee_clothing1 = models.CharField(max_length=200)
    Yankee_adj1 = models.CharField(max_length=200)


class Fortune(models.Model):
    Fortune_verb1 = models.CharField(max_length=200)
    Fortune_verb2 = models.CharField(max_length=200)
    Fortune_adj1 = models.CharField(max_length=200)
    Fortune_adj2 = models.CharField(max_length=200)
    Fortune_adj3 = models.CharField(max_length=200)
    Fortune_noun1 = models.CharField(max_length=200)
    Fortune_noun2 = models.CharField(max_length=200)


class Pizza(models.Model):
    Pizza_name1 = models.CharField(max_length=200)
    Pizza_adj1 = models.CharField(max_length=200)
    Pizza_adj2 = models.CharField(max_length=200)
    Pizza_noun1 = models.CharField(max_length=200)
    Pizza_noun2 = models.CharField(max_length=200)
    Pizza_noun3 = models.CharField(max_length=200)
    Pizza_verb1 = models.CharField(max_length=200)


class Baseball(models.Model):
    Baseball_noun1 = models.CharField(max_length=200)
    Baseball_noun2 = models.CharField(max_length=200)
    Baseball_verb1 = models.CharField(max_length=200)
    Baseball_verb2 = models.CharField(max_length=200)
    Baseball_job1 = models.CharField(max_length=200)
    Baseball_number1 = models.IntegerField()
    Baseball_loc1 = models.CharField(max_length=200)


class VideoGame(models.Model):
    VideoGame_adj1 = models.CharField(max_length=200)
    VideoGame_adj2 = models.CharField(max_length=200)
    VideoGame_name1 = models.CharField(max_length=200)
    VideoGame_job1 = models.CharField(max_length=200)
    VideoGame_verb1 = models.CharField(max_length=200)
    VideoGame_noun1 = models.CharField(max_length=200)
    VideoGame_noun2 = models.CharField(max_length=200)



