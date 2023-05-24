from django.shortcuts import render, redirect
from django.contrib import messages
from .controllers import *
from .forms import *


def render_main_page(request):
    category_id = request.GET.get('id')
    if category_id:
        questions = get_all_questions_with_answers_for_category(category_id)
    else:
        questions = get_all_questions_with_answers()
    question_form = QuestionForm()
    return render(request, 'main.html', context={'questions': questions,
                                                 'question_form': question_form})


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            create_question_with_success_message(form, request)
        else:
            messages.error(request, 'There was an error while adding question, check your data and try again.')
        return redirect('/')


def create_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            create_answer_with_success_message(form, request)
        else:
            messages.error(request, 'There was an error while adding answer, check your data and try again.')
        return redirect('/')


def render_categories_page(request):
    return render(request, 'categories.html', {'categories': get_all_categories()})


def render_question_page(request):
    question_id = request.GET.get('id')
    answer_form = AnswerForm()
    return render(request, 'question.html', {'question': get_question_by_id(question_id),
                                             'answers': get_answers_for_question(question_id),
                                             'answer_form': answer_form})


def render_edit_page(request):
    question_id = request.GET.get('id')
    question = get_question_by_id(question_id)
    edit_form = EditForm()
    return render(request, 'edit_page.html', {'question': question, "edit_form": edit_form})

def edit_question(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            question_id = request.POST.get('pk')
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            category = form.cleaned_data['category']
            edit_question_with_success_message(request, question_id, title, text, category)
        else:
            messages.error(request, 'There was an error while editing the question, check your data and try again.')
        return redirect('/')
