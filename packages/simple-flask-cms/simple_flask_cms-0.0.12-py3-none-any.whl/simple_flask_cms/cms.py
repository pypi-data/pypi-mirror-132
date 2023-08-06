# print("Starting")
import functools
import io
import json
import mimetypes
import os
import random
import string

import bleach
import flask
from flask import Blueprint, render_template, request, abort, Response, url_for, send_from_directory
import markdown
import PIL.Image as pil_image

from . import db
from . import dataclasses
from werkzeug.utils import secure_filename
import typing

cms = Blueprint(
    'simple_flask_cms',
    '__name__',
    static_folder='simple_flask_cms/static',
    template_folder='simple_flask_cms/templates',
    url_prefix='/cms'
)


def require_authentication(func):
    @functools.wraps(func)
    def _inner(*args, **kwargs):
        result = authentication_function(
            action=func.__name__,
            parameters=kwargs
        )
        if result is not None:
            return result

        return func(*args, **kwargs)

    return _inner


def generate_nav(pages):
    nav = []
    page_stack = []
    page_name_stack = []

    for page in pages:
        page.subpages = []
        parts = page.path.split('/')
        max_index = 0
        for index, (path_variable, part_variable) in enumerate(zip(page_name_stack, parts)):
            if path_variable != part_variable:
                break

            max_index = index + 1
        print("max_index", max_index)
        del page_stack[max_index:]
        del page_name_stack[max_index:]

        if len(page_stack) == 0:
            assert max_index == 0
            nav.append(page)
        else:
            assert max_index != 0
            page_stack[-1].subpages.append(page)
            page_stack[-1].subpages.sort(key=lambda i: i.sort_order)

        if len(parts) > max_index:
            page_name_stack.extend(parts[max_index:])
            assert len(page_name_stack) == len(parts)
            while len(page_stack) < len(parts) - 1:
                page_stack.append(page_stack[-1])
            page_stack.append(page)

    nav.sort(key=lambda i: i.sort_order)
    return nav


@cms.route('/editor/<path:path>', methods=['GET', 'POST'])
@require_authentication
def editor(path):
    pages = list(db_connection.get_all_pages())

    if request.method == 'POST':
        data = request.json

        if data is None:
            return 'Invalid JSON', 400

        post = dataclasses.Page(
            **data,
            path=path
        )

        result = db_connection.save_page(post)
        print(result)

    nav[:] = generate_nav(pages)

    images = db_connection.get_images_for_page(path)

    page = db_connection.get_page(path)

    return render_template("cms/main.html", nav=nav, current_page=page, url=path, images=images)


@cms.route("admin/images", methods=["POST"])
@require_authentication
def upload_image():
    page = str(request.headers.get("X-Page"))[:50]
    if not page:
        return "Invalid page", 400
    content_type = request.content_type
    if content_type not in image_content_types:
        return "Invalid Image", 400

    data = io.BytesIO(request.get_data(as_text=False))

    # Make sure the file is a valid image, recognized by PIL
    pil_image.open(data).load()

    filename = secure_filename(request.headers.get("X-Filename", '')).replace('.', '')
    if not filename:
        return "Invalid Request", 400
    filename += mimetypes.guess_extension(content_type, False)

    while os.path.isfile(os.path.join(upload_folder, filename)):
        filename = random.choice(string.ascii_lowercase) + filename

    with open(os.path.join(upload_folder, filename), 'wb') as f:
        data.seek(0)
        f.write(data.read())

    db_connection.save_image(
        dataclasses.Image(
            file=filename,
            page=page,
            mime_type=content_type,
            size=data.getbuffer().nbytes
        )
    )

    return Response(
        json.dumps({
            "path": url_for("simple_flask_cms.get_image", path=filename),
            "filename": filename
        })
    )


@cms.route("admin/images/delete/<string:filename>", methods=["POST"])
@require_authentication
def delete_image(filename):
    filename = secure_filename(filename)
    if not os.path.isfile(os.path.join(upload_folder, filename)):
        return "File not found", 400

    image = db_connection.get_image(filename)

    if image is None:
        return "File not in database", 400

    os.unlink(os.path.join(os.path.join(upload_folder, filename)))
    db_connection.delete_image(
        filename
    )

    return "deleted", 200


@cms.route("images/<string:path>")
def get_image(path):
    return send_from_directory(upload_folder, path)


@cms.route("admin/images/list")
@require_authentication
def list_images():
    images = db_connection.get_all_images()

    return render_template('cms/images.html', images=images, nav=nav)


@cms.route("<path:path>")
def page(path):
    page = db_connection.get_page(path)

    if page is None:
        abort(404)

    page.html = bleach.clean(markdown.markdown(
        page.content,
        extensions=['fenced_code', 'codehilite', 'tables']
    ),
        tags=bleach.ALLOWED_TAGS + [
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
            'span'
        ],
        attributes={
            **bleach.ALLOWED_ATTRIBUTES,
            'img': ['src', 'alt'],
            'div': ['class'],
            'span': ['class']
        }
    )

    return render_template(
        template_name,
        page=page,
        nav=nav
    )


@cms.before_app_first_request
def setup_db():
    if db_connection is None:
        raise ValueError("Set a database before starting the CMS")

    pages = db_connection.get_all_pages()
    nav[:] = generate_nav(pages)


def noop_authentication_function(action, parameters) -> typing.Optional[flask.Response]:
    return None


db_connection: typing.Optional[db.DatabaseProvider] = None
template_name = 'page.html'
nav = []
upload_folder = 'media/cms'
authentication_function = noop_authentication_function

image_content_types = [
    'image/jpeg',
    'image/jpg',
    'image/png',
    'application/png',
    'image/webp',
    'image/gif',
    'image/tif',
    'image/tiff',
]
