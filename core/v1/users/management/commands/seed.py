from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from ...models import Role

User = get_user_model()


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **options):
        admin_role = None

        if not Role.objects.filter(name="ADMIN").exists():
            admin_role = Role.objects.create(
                name="ADMIN", description="Administrator role"
            )
            Role.objects.create(name="USER", description="User role")
            self.stdout.write(self.style.SUCCESS("Roles created successfully"))
        else:
            admin_role = Role.objects.get(name="ADMIN")
            self.stdout.write(self.style.WARNING("Admin role already exists"))

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                is_staff=True,
                password="adminpassword",
                role=admin_role,
            )
            self.stdout.write(self.style.SUCCESS("Successfully created admin user"))
        else:
            self.stdout.write(self.style.WARNING("Admin user already exists"))
