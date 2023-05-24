from django.urls import path
from .views import render_main_page, create_question, render_categories_page, \
    create_answer, render_question_page, render_edit_page, edit_question

urlpatterns = [
    path('', render_main_page, name='render_main_page'),
    path('create_question', create_question, name='create_question'),
    path('create_answer', create_answer, name='create_answer'),
    path('categories', render_categories_page, name='render_categories_page'),
    path('question', render_question_page, name='render_question_page'),
    path('edit', render_edit_page, name='render_edit_page'),
    path('edit_question', edit_question, name='edit_question'),
]
