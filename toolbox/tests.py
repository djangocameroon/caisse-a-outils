from django.test import TestCase
from django.urls import reverse

from . import data, resources


class ToolboxViewsTests(TestCase):
    def setUp(self):
        data.load_tools.cache_clear()
        resources.load_resources.cache_clear()

    def test_home_page_renders_with_hero(self):
        response = self.client.get(reverse("toolbox:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Caisse A Outils centralise les astuces")

    def test_tool_list_page_renders(self):
        response = self.client.get(reverse("toolbox:tool_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Outils recommandés")

    def test_tool_detail_page_renders_markdown_content(self):
        tool = data.get_all_tools()[0]
        response = self.client.get(reverse("toolbox:tool_detail", args=[tool.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, tool.name)
        self.assertContains(response, "Mise en route")

    def test_resource_list_page_renders(self):
        response = self.client.get(reverse("toolbox:resource_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ressources partagées en JSON")

    def test_resource_detail_page_renders_content(self):
        resource = resources.get_all_resources()[0]
        response = self.client.get(reverse("toolbox:resource_detail", args=[resource.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, resource.title)
        self.assertContains(response, "Commandes incontournables")
