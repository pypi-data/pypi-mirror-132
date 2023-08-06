import pydantic
import datetime
from typing import NamedTuple
import typing

from flask import url_for


class FragmentType(NamedTuple):
    name: str
    description: typing.Optional[str]
    url: typing.Optional[str]


class StrippedPage(pydantic.BaseModel):
    path: str
    title: str
    nav_title: str
    sort_order: int
    date_modified: datetime.datetime
    subpages: list = []

    def is_special_page(self):
        return False

    def get_absolute_url(self):
        return url_for("simple_flask_cms.page", path=self.path)


class Page(StrippedPage):
    content: str
    html: str = ""


class Image(pydantic.BaseModel):
    file: str
    page: str
    mime_type: str
    size: int


class StrippedFragment(pydantic.BaseModel):
    name: str
    date_modified: datetime.datetime
    fragment_type: typing.Optional[FragmentType] = None


class Fragment(StrippedFragment):
    content: str
    html: str = ""


class ExtraNavUrl(pydantic.BaseModel):
    path: str
    redirect: str
    nav_title: str
    subpages: list = []
    sort_order: int = 30

    @pydantic.validator('path')
    def must_not_start_with_slash(cls, v):
        if v.startswith('/'):
            raise ValueError('The path must not start with a slash. Consider removing the leading /')
        return v

    def is_special_page(self):
        return True

    def get_absolute_url(self):
        return self.redirect
