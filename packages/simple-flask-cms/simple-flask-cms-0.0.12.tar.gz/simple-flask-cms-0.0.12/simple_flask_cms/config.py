import typing
import flask
from . import db
from . import dataclasses


def noop_authentication_function(action, parameters) -> typing.Optional[flask.Response]:
    return None


editor_paths = [
    'editor', 'upload_image', 'delete_image', 'list_images', 'delete_page', 'fragment',
    'editor_home']
viewer_paths = ['page', 'get_image']

db_connection: typing.Optional[db.DatabaseProvider] = None
template_name = 'cms/example_templates/page.html'
upload_folder = 'media/cms'
authentication_function = noop_authentication_function
enable_custom_404 = True
fragments: typing.List[dataclasses.FragmentType] = []

markdown_extensions = ['fenced_code', 'codehilite', 'tables']
markdown_extra_tags = [
    'img',
    'a',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'p',
    'br',
    'pre',
    'div',
    'span',
    'table',
    'tr',
    'th',
    'th'
]
markdown_extra_attrs = {
    'img': ['src', 'alt'],
    'div': ['class'],
    'span': ['class']
}

"""
Provides extra context for the page template
"""
extra_page_content_provider = lambda path: {}

extra_nav_urls: typing.List[dataclasses.ExtraNavUrl] = []
