"""Utility script for creating and deleting fake poll data.

This script is intended for local development and testing. It creates
sample Question and Choice objects in the Django database so the app can
be tested with realistic sample content.
"""

import os
import random

import django
from django.conf import settings
from django.utils import timezone
from faker import Faker

# Set up Django so the script can interact with the project database.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Question, Choice

# Initialize Faker for creating realistic text and timestamps.
fake = Faker()

# Get the project's timezone settings for dates generated in the app's locale.
project_timezone = settings.TIME_ZONE


def create_100_entries():
    """Create 100 questions with topic-based choices for testing."""
    # Define a list of categories used to generate realistic question topics.
    topics = [
        "Technology",
        "Science",
        "Movies",
        "Music",
        "Food",
        "Travel",
        "Sports",
        "Books",
        "History"
    ]

    # Map each topic to related answer choices so generated data feels consistent.
    choices_by_topic = {
        "Technology": ["Python", "JavaScript", "Web Development", "Data Science", "AI"],
        "Science": ["Biology", "Physics", "Chemistry", "Astronomy", "Geology"],
        "Movies": ["Action", "Comedy", "Drama", "Science Fiction", "Fantasy"],
        "Music": ["Rock", "Pop", "Hip-Hop", "Jazz", "Classical"],
        "Food": ["Italian", "Mexican", "Indian", "Sushi", "Vegan"],
        "Travel": ["Beaches", "Mountains", "Cities", "Adventure", "Cultural"],
        "Sports": ["Soccer", "Basketball", "Tennis", "Swimming", "Golf"],
        "Books": ["Mystery", "Romance", "Fantasy", "Science Fiction", "Non-Fiction"],
        "History": ["Ancient Civilizations", "World Wars", "Medieval Europe", "Ancient Rome", "Renaissance"]
    }

    # Create 100 questions with meaningful choices to simulate real application data.
    for _ in range(100):
        topic = random.choice(topics)
        q_text = "%s: %s" % (topic, fake.sentence(nb_words=10, variable_nb_words=True))

        # Generate a datetime in the project's timezone so entries match the app settings.
        pub_date = fake.date_time_between(start_date='-30d', end_date='now', tzinfo=timezone.get_current_timezone())
        question = Question.objects.create(question_text=q_text.replace('.','?'), pub_date=pub_date)
        print("# %s" % question)

        # Attach answer options that fit the selected topic.
        choices = choices_by_topic[topic]
        for choice_text in choices:
            choice1 = Choice.objects.create(question=question, choice_text=choice_text)
            print(" - %s" % choice1)
        print('# ----')

    print("100 entries have been created successfully.")


def delete_entries():
    """Delete all question records except the first entry."""
    try:
        # Delete entries where id > 1 to leave a single baseline record.
        deleted_count, deleted_entries = Question.objects.filter(id__gt=1).delete()
        print("Deleted entries: %s" % deleted_entries)
        print(f"Deleted {deleted_count} Question entries where id > 1")
    except Question.DoesNotExist:
        print("No entries found to delete.")


if __name__ == '__main__':
    # Display a small console menu for manual testing and cleanup.
    while True:
        print("\nMenu:")
        print("1. Create 100 entries")
        print("2. Delete all entries with id > 1")
        print("0. Exit")

        chosen = input("Enter your choice: ")

        if chosen == "1":
            create_100_entries()
        elif chosen == "2":
            delete_entries()
        elif chosen == "0":
            print("Goodbye! Nothing has been done")
            break
        else:
            print("Invalid choice. Please select a valid option.")
