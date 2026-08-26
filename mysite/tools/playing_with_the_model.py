# # -*- coding: UTF-8 -*-
# # template to deal with Django model programmatically
# # Name: wolke
# # Datum: 13.09.26
# # macOS 26.5.1  Python 3.14
#
# Import necessary modules
import os
import sys

import django
from django.utils import timezone

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()


print('Python: %s on platform: %s' % (sys.version, sys.platform))
print('Django version: %s' % django.get_version())
print("Django Environment variable DJANGO_SETTINGS_MODULE is set to: '%s'" % (os.getenv("DJANGO_SETTINGS_MODULE")))
print("Timezone is set to: %s" % timezone.get_current_timezone_name())
print("Localtime is: %s" % timezone.localtime())
print("UTC time is: %s" % timezone.now())

# Import the Question and Choice models after django.setup()
from polls.models import Question, Choice


# Function to print all questions and their choices
def print_questions_and_choices():
    # Retrieve all questions
    questions = Question.objects.all()

    # Loop through questions and print their choices
    for question in questions:
        print(f"Question: {question.question_text}")
        choices = Choice.objects.filter(question=question)
        for choice in choices:
            print(f" - Choice: {choice.choice_text:25s}| Votes: {choice.votes}")
        print()


# Create a new question and choices
def create_question_with_choices(question_text, choice_texts):
    # Create a new question
    question = Question.objects.create(question_text=question_text, pub_date=timezone.now())

    # Create choices for the question
    for choice_text in choice_texts:
        Choice.objects.create(question=question, choice_text=choice_text)


if __name__ == "__main__":
    # Print all existing questions and choices
    print("Existing Questions and Choices:")
    print_questions_and_choices()

    # Create a new question with choices
    new_question_text = "What's your favorite programming language?"
    new_choice_texts = ["Python", "Java", "JavaScript"]
    create_question_with_choices(new_question_text, new_choice_texts)
