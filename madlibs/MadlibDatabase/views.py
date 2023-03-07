from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BeKind, SickNote, Greetings, CatFiddle, Katie, NewDay, IndustryAward, Tolkien, BlindMice, Valentine
from .models import Yankee, Fortune, Pizza, Baseball, VideoGame
from django.template import loader
from .forms import BeKindForm, SickNoteForm, GreetingsForm, CatFiddleForm, KatieForm, NewDayForm, IndustryAwardForm
from .forms import TolkienForm, BlindMiceForm, ValentineForm, YankeeForm, FortuneForm, PizzaForm, BaseballForm, VideoGameForm


# Create your views here.
def index(request):
    context = {}
    return render(request, 'home/index.html', context)


def be_kind(request):
    be_kind_list = BeKind.objects.all()
    context = {
        'be_kind_list': be_kind_list
    }
    return render(request, 'be_kind/madlib.html', context)


def be_kind_form(request):
    BeKind.objects.all().delete()
    form = BeKindForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('be_kind')

    return render(request, 'be_kind/form.html', {'form': form})


def sick_note(request):
    sick_note_list = SickNote.objects.all()

    context = {
        'sick_note_list': sick_note_list,
    }
    return render(request, 'sick_note/madlibs.html', context)


def sick_note_form(request):
    SickNote.objects.all().delete()
    form = SickNoteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('sick_note')

    return render(request, 'sick_note/form.html', {'form': form})


def greetings(request):
    greetings_list = Greetings.objects.all()

    context = {
        'greetings_list': greetings_list,
    }
    return render(request, 'greetings/madlibs.html', context)


def greetings_form(request):
    Greetings.objects.all().delete()
    form = GreetingsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('greetings')

    return render(request, 'greetings/form.html', {'form': form})


def cat_fiddle(request):
    cat_fiddle_list = CatFiddle.objects.all()

    context = {
        'cat_fiddle_list': cat_fiddle_list,
    }
    return render(request, 'cat_fiddle/madlibs.html', context)


def cat_fiddle_form(request):
    CatFiddle.objects.all().delete()
    form = CatFiddleForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cat_fiddle')

    return render(request, 'cat_fiddle/form.html', {'form': form})


def katie(request):
    katie_list = Katie.objects.all()

    context = {
        'katie_list': katie_list,
    }
    return render(request, 'katie/madlibs.html', context)


def katie_form(request):
    Katie.objects.all().delete()
    form = KatieForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('katie')

    return render(request, 'katie/form.html', {'form': form})


def new_day(request):
    new_day_list = NewDay.objects.all()

    context = {
        'new_day_list': new_day_list,
    }
    return render(request, 'new_day/madlibs.html', context)


def new_day_form(request):
    NewDay.objects.all().delete()
    form = NewDayForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('new_day')

    return render(request, 'new_day/form.html', {'form': form})


def industry_award(request):
    industry_award_list = IndustryAward.objects.all()

    context = {
        'industry_award_list': industry_award_list,
    }
    return render(request, 'industry_award/madlibs.html', context)


def industry_award_form(request):
    IndustryAward.objects.all().delete()
    form = IndustryAwardForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('industry_award')

    return render(request, 'industry_award/form.html', {'form': form})


def tolkien(request):
    tolkien_list = Tolkien.objects.all()
    context = {
        'tolkien_list': tolkien_list,
    }
    return render(request, 'tolkien/madlibs.html', context)


def tolkien_form(request):
    Tolkien.objects.all().delete()
    form = TolkienForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('tolkien')

    return render(request, 'tolkien/form.html', {'form': form})


def blind_mice(request):
    blind_mice_list = BlindMice.objects.all()

    context = {
        'blind_mice_list': blind_mice_list,
    }
    return render(request, 'blind_mice/madlibs.html', context)


def blind_mice_form(request):
    BlindMice.objects.all().delete()
    form = BlindMiceForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('blind_mice')

    return render(request, 'blind_mice/form.html', {'form': form})


def valentine(request):
    valentine_list = Valentine.objects.all()

    context = {
        'valentine_list': valentine_list,
    }
    return render(request, 'valentine/madlibs.html', context)


def valentine_form(request):
    Valentine.objects.all().delete()
    form = ValentineForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('valentine')

    return render(request, 'valentine/form.html', {'form': form})


def yankee(request):
    yankee_list = Yankee.objects.all()

    context = {
        'yankee_list': yankee_list,
    }
    return render(request, 'yankee/madlibs.html', context)


def yankee_form(request):
    Yankee.objects.all().delete()
    form = YankeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('yankee')

    return render(request, 'yankee/form.html', {'form': form})


def fortune(request):
    fortune_list = Fortune.objects.all()

    context = {
        'fortune_list': fortune_list,
    }
    return render(request, 'fortune/madlibs.html', context)


def fortune_form(request):
    Fortune.objects.all().delete()
    form = FortuneForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('fortune')

    return render(request, 'fortune/form.html', {'form': form})


def pizza(request):
    pizza_list = Pizza.objects.all()

    context = {
        'pizza_list': pizza_list,
    }
    return render(request, 'pizza/madlibs.html', context)


def pizza_form(request):
    Pizza.objects.all().delete()
    form = PizzaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('pizza')

    return render(request, 'pizza/form.html', {'form': form})


def baseball(request):
    baseball_list = Baseball.objects.all()

    context = {
        'baseball_list': baseball_list,
    }
    return render(request, 'baseball/madlibs.html', context)


def baseball_form(request):
    Baseball.objects.all().delete()
    form = BaseballForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('baseball')

    return render(request, 'baseball/form.html', {'form': form})


def video_game(request):
    video_game_list = VideoGame.objects.all()

    context = {
        'video_game_list': video_game_list,
    }
    return render(request, 'video_game/madlibs.html', context)


def video_game_form(request):
    VideoGame.objects.all().delete()
    form = VideoGameForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('video_game')

    return render(request, 'video_game/form.html', {'form': form})


