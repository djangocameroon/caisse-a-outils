from django.http import Http404
from django.shortcuts import render

from .data import get_all_tools, get_tool
from .resources import get_all_resources, get_resource


def home(request):
    tools = get_all_tools()
    resources = get_all_resources()
    context = {
        "hero_tools": tools[:4],
        "hero_resources": resources[:3],
    }
    return render(request, "toolbox/home.html", context)


def tool_list(request):
    tools = get_all_tools()
    return render(request, "toolbox/tool_list.html", {"tools": tools})


def tool_detail(request, slug: str):
    try:
        tool = get_tool(slug)
    except KeyError as exc:
        raise Http404("Outil introuvable") from exc
    return render(request, "toolbox/tool_detail.html", {"tool": tool})


def resource_list(request):
    resources = get_all_resources()
    return render(request, "toolbox/resource_list.html", {"resources": resources})


def resource_detail(request, slug: str):
    try:
        resource = get_resource(slug)
    except KeyError as exc:
        raise Http404("Ressource introuvable") from exc
    return render(request, "toolbox/resource_detail.html", {"resource": resource})
