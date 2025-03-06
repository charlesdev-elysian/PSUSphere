from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember
import random

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting data generation...')
        self.create_colleges(5)
        self.create_programs(10)
        self.create_organizations(10)
        self.create_students(50)
        self.create_memberships(20)
        self.stdout.write(self.style.SUCCESS('Data generation completed successfully.'))

    def create_colleges(self, count):
        fake = Faker()
        for _ in range(count):
            College.objects.create(college_name=fake.company())
        self.stdout.write(self.style.SUCCESS(f'Created {count} colleges.'))

    def create_programs(self, count):
        fake = Faker()
        colleges = list(College.objects.all())
        for _ in range(count):
            Program.objects.create(
                prog_name=fake.job(),
                college=random.choice(colleges)
            )
        self.stdout.write(self.style.SUCCESS(f'Created {count} programs.'))

    def create_organizations(self, count):
        fake = Faker()
        colleges = list(College.objects.all())
        for _ in range(count):
            Organization.objects.create(
                name=fake.catch_phrase(),
                college=random.choice(colleges),
                description=fake.text(max_nb_chars=200)
            )
        self.stdout.write(self.style.SUCCESS(f'Created {count} organizations.'))

    def create_students(self, count):
        fake = Faker('en_PH')
        programs = list(Program.objects.all())
        for _ in range(count):
            Student.objects.create(
                student_id=f"{fake.random_int(2020, 2024)}-{fake.random_int(1, 8)}-{fake.random_number(digits=4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=random.choice(programs)
            )
        self.stdout.write(self.style.SUCCESS(f'Created {count} students.'))