from django.core.management.base import BaseCommand
from pybo.utils import fetch_and_parse_notion_data

class Command(BaseCommand):
    help = 'Fetch data from Notion and save to database'

    def handle(self, *args, **kwargs):
        fetch_and_parse_notion_data()
        self.stdout.write(self.style.SUCCESS('Successfully fetched data from Notion'))
