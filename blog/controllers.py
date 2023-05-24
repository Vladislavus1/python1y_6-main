from django.contrib import messages
from django.shortcuts import get_object_or_404

from .models import Question, Answer, Category


def get_all_questions():
    return Question.objects.all()


def get_all_answers():
    return Answer.objects.all()


def get_all_questions_with_answers_for_category(category_id):
    return Question.objects.all().filter(category=int(category_id)).prefetch_related('answer_set')


def get_question_by_id(question_id):
    return Question.objects.get(pk=question_id)


def get_answers_for_question(question_id):
    return Answer.objects.all().filter(question=question_id)


def get_all_questions_with_answers():
    return Question.objects.all().prefetch_related('answer_set')


def get_all_categories():
    return Category.objects.all()


def create_question_with_success_message(form, request):
    question = form.save(commit=False)
    question.author = request.user
    question.publish()
    messages.success(request, message='Question asked!')


def create_answer_with_success_message(form, request):
    answer = form.save(commit=False)
    answer.author = request.user
    question_pk = request.POST.get('pk')
    print(question_pk)
    question = Question.objects.get(pk=question_pk)
    answer.question = question
    answer.publish()
    messages.success(request, message='Answer asked!')


def edit_question_with_success_message(request, question_id, title, text, category_id):
    question = Question.objects.get(pk=question_id)
    question.title = title
    question.text = text
    question.category_id = category_id
    question.save()
    messages.success(request, message='Question edited!')

