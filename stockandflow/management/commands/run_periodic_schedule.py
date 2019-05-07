from django.core.management.base import BaseCommand
import stockandflow

class Command(BaseCommand):
    args = ""
    help = "Run the periodic schedule entries. This should be called from cron at an interval that equals the shortest period length."

    def handle(self, *args, **options):
        stockandflow.periodic.schedule.run()
