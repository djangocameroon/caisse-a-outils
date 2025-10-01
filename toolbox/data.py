from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterable

from django.conf import settings
from markdown import markdown


@dataclass(frozen=True)
class Tool:
    slug: str
    name: str
    summary: str
    website: str | None
    categories: tuple[str, ...]
    content_html: str
    content_markdown_path: Path


def _load_markdown(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Markdown file not found: {path}")
    raw = path.read_text(encoding="utf-8")
    return markdown(raw, extensions=["fenced_code", "tables"])  # rich markdown support


@lru_cache
def load_tools() -> tuple[Tool, ...]:
    data_file = settings.DATA_DIR / "tools.json"
    if not data_file.exists():
        raise FileNotFoundError("The tools.json data file is missing.")

    raw_tools: Iterable[dict[str, object]] = json.loads(data_file.read_text(encoding="utf-8"))
    tools: list[Tool] = []

    for entry in raw_tools:
        slug = str(entry.get("slug", "")).strip()
        if not slug:
            continue
        name = str(entry.get("name", slug)).strip()
        summary = str(entry.get("summary", "")).strip()
        website = entry.get("website")
        if isinstance(website, str):
            website = website.strip() or None
        categories = entry.get("categories") or []
        if not isinstance(categories, list):
            categories = [str(categories)]
        categories_tuple = tuple(str(cat).strip() for cat in categories if str(cat).strip())

        content_path_value = entry.get("content_path")
        if not isinstance(content_path_value, str):
            raise ValueError(f"Missing markdown path for tool '{slug}'.")
        markdown_path = settings.DATA_DIR / content_path_value
        html_content = _load_markdown(markdown_path)

        tools.append(
            Tool(
                slug=slug,
                name=name,
                summary=summary,
                website=website,
                categories=categories_tuple,
                content_html=html_content,
                content_markdown_path=markdown_path,
            )
        )

    return tuple(tools)


def get_all_tools() -> tuple[Tool, ...]:
    return load_tools()


def get_tool(slug: str) -> Tool:
    slug = slug.strip().lower()
    for tool in load_tools():
        if tool.slug.lower() == slug:
            return tool
    raise KeyError(f"Unknown tool slug: {slug}")
