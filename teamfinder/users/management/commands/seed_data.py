from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from projects.models import Project

User = get_user_model()


class Command(BaseCommand):
    help = "Seed test data"

    def handle(self, *args, **kwargs):

        User.objects.all().delete()
        Project.objects.all().delete()

        user1 = User.objects.create_user(
            email="user1@test.com",
            password="12345678",
            name="Мирослава",
            surname="Жиздюк",
            phone="1000000001",
        )

        user2 = User.objects.create_user(
            email="user2@test.com",
            password="12345678",
            name="Маша",
            surname="Тест1",
            phone="1000000002",
        )

        user3 = User.objects.create_user(
            email="user3@test.com",
            password="12345678",
            name="Анна",
            surname="Тест2",
            phone="1000000003",
        )

        project1 = Project.objects.create(
            name="Django Team",
            description="Создан с помощью Django",
            owner=user1,
        )

        project2 = Project.objects.create(
            name="React App",
            description="Фронтенд проект",
            owner=user2,
        )

        project3 = Project.objects.create(
            name="AI Project",
            description="LLM моделька",
            owner=user3,
        )

        project1.participants.add(user2, user3)
        project2.participants.add(user1)
        project3.participants.add(user1, user2)

        user1.favorites.add(project2, project3)
        user2.favorites.add(project1)
        user3.favorites.add(project1, project2)

        self.stdout.write(self.style.SUCCESS("Seed created successfully"))
