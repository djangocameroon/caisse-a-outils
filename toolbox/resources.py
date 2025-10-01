from __future__ import annotations

import json
import tomllib
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterable

import yaml
from django.conf import settings
from markdown import markdown


@dataclass(frozen=True)
class Resource:
    slug: str
    title: str
    summary: str
    categories: tuple[str, ...]
    content_html: str
    source_file: Path
    source_format: str


def _normalize_categories(raw: object) -> tuple[str, ...]:
    if raw is None:
        return ()
    if isinstance(raw, (list, tuple)):
        items: Iterable[str] = (str(item).strip() for item in raw if str(item).strip())
        return tuple(items)
    text = str(raw).strip()
    return (text,) if text else ()


def _render_markdown(value: str, origin: Path) -> str:
    if not value.strip():
        raise ValueError(f"Markdown content is empty in {origin}")
    return markdown(value, extensions=["fenced_code", "tables"])


def _read_markdown_from_path(relative_path: str, base: Path, origin: Path) -> str:
    markdown_path = base / relative_path
    if not markdown_path.exists():
        raise FileNotFoundError(f"Markdown file not found for resource defined in {origin}: {markdown_path}")
    raw = markdown_path.read_text(encoding="utf-8")
    return _render_markdown(raw, markdown_path)


def _coerce_to_sequence(data: object) -> Iterable[dict[str, object]]:
    if isinstance(data, dict):
        return [data]
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    raise ValueError("Unsupported resource payload; expected dict or list of dicts")


def _parse_file(path: Path) -> Iterable[dict[str, object]]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
    elif suffix in {".yaml", ".yml"}:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    elif suffix == ".toml":
        payload = tomllib.loads(path.read_text(encoding="utf-8"))
        content_block = payload.get("content")
        if isinstance(content_block, dict) and "markdown" in content_block:
            payload["body"] = content_block.get("markdown")
    else:
        raise ValueError(f"Unsupported resource format: {path.suffix}")
    return _coerce_to_sequence(payload)


@lru_cache
def load_resources() -> tuple[Resource, ...]:
    resources_dir = settings.DATA_DIR / "resources"
    if not resources_dir.exists():
        return ()

    resources: list[Resource] = []
    for path in sorted(resources_dir.iterdir()):
        if path.suffix.lower() not in {".json", ".yaml", ".yml", ".toml"}:
            continue
        entries = _parse_file(path)
        for entry in entries:
            slug = str(entry.get("slug", "")).strip()
            if not slug:
                continue
            title = str(entry.get("title", slug)).strip()
            summary = str(entry.get("summary", "")).strip()
            categories = _normalize_categories(entry.get("categories"))

            body_markdown = entry.get("body") or entry.get("content")
            content_path = entry.get("content_path")

            if isinstance(content_path, str) and content_path.strip():
                content_html = _read_markdown_from_path(content_path.strip(), settings.DATA_DIR, path)
            elif isinstance(body_markdown, str):
                content_html = _render_markdown(body_markdown, path)
            else:
                raise ValueError(f"Resource '{slug}' defined in {path} has no markdown content")

            resources.append(
                Resource(
                    slug=slug,
                    title=title,
                    summary=summary,
                    categories=categories,
                    content_html=content_html,
                    source_file=path,
                    source_format=path.suffix.lstrip("."),
                )
            )

    resources.sort(key=lambda item: item.title.lower())
    return tuple(resources)


def get_all_resources() -> tuple[Resource, ...]:
    return load_resources()


def get_resource(slug: str) -> Resource:
    slug = slug.strip().lower()
    for resource in load_resources():
        if resource.slug.lower() == slug:
            return resource
    raise KeyError(f"Unknown resource slug: {slug}")
