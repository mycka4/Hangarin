from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from tasks.models import Priority, Category, Task, Note, SubTask

class Command(BaseCommand):
    help = 'Seed fake data for Hangarin'

    def handle(self, *args, **kwargs):
        self.seed_priorities()
        self.seed_categories()
        self.create_tasks(10)
        self.create_notes(10)
        self.create_subtasks(10)

    def seed_priorities(self):
        priorities = ['High', 'Medium', 'Low', 'Critical', 'Optional']
        for p in priorities:
            Priority.objects.get_or_create(name=p)
        self.stdout.write(self.style.SUCCESS('Priorities created successfully.'))

    def seed_categories(self):
        categories = ['Work', 'School', 'Personal', 'Finance', 'Projects']
        for c in categories:
            Category.objects.get_or_create(name=c)
        self.stdout.write(self.style.SUCCESS('Categories created successfully.'))

    def create_tasks(self, count):
        fake = Faker()
        for _ in range(count):
            Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                category=Category.objects.order_by('?').first(),
                priority=Priority.objects.order_by('?').first()
            )
        self.stdout.write(self.style.SUCCESS('Tasks created successfully.'))

    def create_notes(self, count):
        fake = Faker()
        for _ in range(count):
            Note.objects.create(
                task=Task.objects.order_by('?').first(),
                content=fake.paragraph(nb_sentences=3)
            )
        self.stdout.write(self.style.SUCCESS('Notes created successfully.'))

    def create_subtasks(self, count):
        fake = Faker()
        for _ in range(count):
            SubTask.objects.create(
                parent_task=Task.objects.order_by('?').first(),
                title=fake.sentence(nb_words=5),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"])
            )
        self.stdout.write(self.style.SUCCESS('Subtasks created successfully.'))