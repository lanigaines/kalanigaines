from typing import Any

from django.template import Template
from django.template.backends.base import BaseEngine

ROOT: Any

def get_default_renderer() -> DjangoTemplates: ...

class BaseRenderer:
    def get_template(self, template_name: str) -> Any: ...
    def render(
        self, template_name: str, context: dict[str, Any], request: None = ...
    ) -> str: ...

class EngineMixin:
    def get_template(self, template_name: str) -> Any: ...
    def engine(self) -> BaseEngine: ...

class DjangoTemplates(EngineMixin, BaseRenderer):
    backend: Any = ...

class Jinja2(EngineMixin, BaseRenderer):
    backend: Any = ...

class TemplatesSetting(BaseRenderer):
    def get_template(self, template_name: str) -> Template: ...
