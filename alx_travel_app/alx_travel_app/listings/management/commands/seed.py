from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        titles = ['Beach House', 'Mountain Cabin', 'City Apartment', 'Country Home']
        locations = ['Dakar', 'Paris', 'New York', 'Tokyo']

        for _ in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description='A wonderful place to stay.',
                location=random.choice(locations),
                price_per_night=random.randint(50, 300),
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings'))
