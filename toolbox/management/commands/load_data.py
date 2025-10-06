from django.core.management.base import BaseCommand
from toolbox.data import get_all_tools
from toolbox.resources import get_all_resources
from toolbox.models import Tool, Resource

class Command(BaseCommand):
    help = 'Load tools and resources from data files into the database.'

    def handle(self, *args, **options):
        self.stdout.write('Loading tools...')
        Tool.objects.all().delete()
        for tool in get_all_tools():
            Tool.objects.create(
                slug=tool.slug,
                name=tool.name,
                summary=tool.summary,
                website=tool.website,
                categories=list(tool.categories),
                content_html=tool.content_html,
                content_markdown_path=str(tool.content_markdown_path),
            )
        self.stdout.write(self.style.SUCCESS(f'Loaded {Tool.objects.count()} tools.'))

        self.stdout.write('Loading resources...')
        Resource.objects.all().delete()
        for resource in get_all_resources():
            Resource.objects.create(
                slug=resource.slug,
                title=resource.title,
                summary=resource.summary,
                categories=list(resource.categories),
                content_html=resource.content_html,
                source_file=str(resource.source_file),
                source_format=resource.source_format,
            )
        self.stdout.write(self.style.SUCCESS(f'Loaded {Resource.objects.count()} resources.'))
