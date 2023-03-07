from django import forms
from .models import BeKind, SickNote, Greetings, CatFiddle, Katie, NewDay, IndustryAward, Tolkien, BlindMice, Valentine
from .models import Yankee, Fortune, Pizza, Baseball, VideoGame


class BeKindForm(forms.ModelForm):
    class Meta:
        model = BeKind
        fields = ['BeKind_noun1', 'BeKind_noun2', 'BeKind_noun3', 'BeKind_noun_plural1', 'BeKind_adj1', 'BeKind_adj2',
                  'BeKind_place1']


class SickNoteForm(forms.ModelForm):
    class Meta:
        model = SickNote
        fields = ['SickNote_word1', 'SickNote_word2', 'SickNote_name1', 'SickNote_illness1', 'SickNote_noun_plural1',
                  'SickNote_adj1', 'SickNote_adj2']


class GreetingsForm(forms.ModelForm):
    class Meta:
        model = Greetings
        fields = ['Greetings_noun_plural1', 'Greetings_occupation1', 'Greetings_animal_plural1', 'Greetings_adj1',
                  'Greetings_place1', 'Greetings_verb1', 'Greetings_noun1']


class CatFiddleForm(forms.ModelForm):
    class Meta:
        model = CatFiddle
        fields = ['CatFiddle_word1', 'CatFiddle_animal1', 'CatFiddle_instrument1', 'CatFiddle_adj1',
                  'CatFiddle_adj2', 'CatFiddle_noun1', 'CatFiddle_noun2']


class KatieForm(forms.ModelForm):
    class Meta:
        model = Katie
        fields = ['Katie_verb1', 'Katie_verb2', 'Katie_verb3', 'Katie_noun1',
                  'Katie_part1', 'Katie_animal1', 'Katie_adj1']


class NewDayForm(forms.ModelForm):
    class Meta:
        model = NewDay
        fields = ['NewDay_verb1', 'NewDay_verb2', 'NewDay_verb3', 'NewDay_verb4',
                  'NewDay_verb5', 'NewDay_place1', 'NewDay_adj1']


class IndustryAwardForm(forms.ModelForm):
    class Meta:
        model = IndustryAward
        fields = ['IndustryAward_company1', 'IndustryAward_noun1', 'IndustryAward_noun2', 'IndustryAward_noun3',
                  'IndustryAward_noun4', 'IndustryAward_adj1', 'IndustryAward_adj2']


class TolkienForm(forms.ModelForm):
    class Meta:
        model = Tolkien
        fields = ['Tolkien_fruit1', 'Tolkien_noun1', 'Tolkien_noun2', 'Tolkien_noun3',
                  'Tolkien_noun4', 'Tolkien_noun5', 'Tolkien_word1']


class BlindMiceForm(forms.ModelForm):
    class Meta:
        model = BlindMice
        fields = ['BlindMice_number1', 'BlindMice_adj1', 'BlindMice_verb1', 'BlindMice_job1',
                  'BlindMice_relation1', 'BlindMice_part1', 'BlindMice_noun1']


class ValentineForm(forms.ModelForm):
    class Meta:
        model = Valentine
        fields = ['Valentine_noun1', 'Valentine_noun2', 'Valentine_noun3', 'Valentine_adj1',
                  'Valentine_verb1', 'Valentine_color1', 'Valentine_part1']
