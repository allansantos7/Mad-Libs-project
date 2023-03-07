from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),

    path('be_kind/', views.be_kind, name="be_kind"),
    path('be_kind_form/', views.be_kind_form, name="be_kind_form"),

    path('sick_note/', views.sick_note, name="sick_note"),
    path('sick_note_form/', views.sick_note_form, name="sick_note_form"),

    path('greetings/', views.greetings, name="greetings"),
    path('greetings_form/', views.greetings_form, name="greetings_form"),

    path('cat_fiddle/', views.cat_fiddle, name="cat_fiddle"),
    path('cat_fiddle_form/', views.cat_fiddle_form, name="cat_fiddle_form"),

    path('katie/', views.katie, name="katie"),
    path('katie_form/', views.katie_form, name="katie_form"),

    path('new_day/', views.new_day, name="new_day"),
    path('new_day_form/', views.new_day_form, name="new_day_form"),

    path('industry_award/', views.industry_award, name="industry_award"),
    path('industry_award_form/', views.industry_award_form, name="industry_award_form"),

    path('tolkien/', views.tolkien, name="tolkien"),
    path('tolkien_form/', views.tolkien_form, name="tolkien_form"),

    path('blind_mice/', views.blind_mice, name="blind_mice"),
    path('blind_mice_form/', views.blind_mice_form, name="blind_mice_form"),

    path('valentine/', views.valentine, name="valentine"),
    path('valentine_form/', views.valentine_form, name="valentine_form"),

    path('yankee/', views.yankee, name="yankee"),
    path('yankee_form/', views.yankee_form, name="yankee_form"),

    path('fortune/', views.fortune, name="fortune"),
    path('fortune_form/', views.fortune_form, name="fortune_form"),

    path('pizza/', views.pizza, name="pizza"),
    path('pizza_form/', views.pizza_form, name="pizza_form"),


    path('baseball/', views.baseball, name="baseball"),
    path('baseball_form/', views.baseball_form, name="baseball_form"),

    path('video_game/', views.video_game, name="video_game"),
    path('video_game_form/', views.video_game_form, name="video_game_form"),
]