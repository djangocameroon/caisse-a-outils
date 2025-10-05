from django.http import Http404
from django.shortcuts import render

from .data import get_all_tools, get_tool
from .resources import get_all_resources, get_resource

from .models import Tool, Resource


def home(request):
    tools = Tool.objects.all().order_by("name")
    resources = Resource.objects.all().order_by("title")
    context = {
        "hero_tools": tools[:4],
        "hero_resources": resources[:3],
    }
    return render(request, "toolbox/home.html", context)


def tool_list(request):
    tools = Tool.objects.all().order_by("name")
    return render(request, "toolbox/tool_list.html", {"tools": tools})


def tool_detail(request, slug: str):
    try:
        tool = Tool.objects.get(slug=slug)
    except Tool.DoesNotExist as exc:
        raise Http404("Outil introuvable") from exc
    return render(request, "toolbox/tool_detail.html", {"tool": tool})


def resource_list(request):
    resources = Resource.objects.all().order_by("title")
    return render(request, "toolbox/resource_list.html", {"resources": resources})


def resource_detail(request, slug: str):
    try:
        resource = Resource.objects.get(slug=slug)
    except Resource.DoesNotExist as exc:
        raise Http404("Ressource introuvable") from exc
    return render(request, "toolbox/resource_detail.html", {"resource": resource})
