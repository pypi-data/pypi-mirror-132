import typing

import flask_sqlalchemy
import traceback
from simple_flask_cms import dataclasses
from simple_flask_cms.db import DatabaseProvider


class SQLDatabaseProvider(DatabaseProvider):

    def __init__(self, app, db=None):
        if db is None:
            db = flask_sqlalchemy.SQLAlchemy(app)

        self.db = db

        class Page(db.Model):
            __tablename__ = "cms_page"
            id = db.Column(db.Integer, primary_key=True)
            path = db.Column(db.String(), index=True, unique=True)
            title = db.Column(db.String())
            nav_title = db.Column(db.String())
            sort_order = db.Column(db.Integer)
            hidden = db.Column(db.Boolean)
            content = db.Column(db.UnicodeText)
            date_modified = db.Column(db.DateTime)

        self.Page = Page

        class Image(db.Model):
            __tablename__ = "cms_image"
            id = db.Column(db.Integer(), primary_key=True)
            file = db.Column(db.String(), index=True)
            page = db.Column(db.String())
            mime_type = db.Column(db.String())
            size = db.Column(db.String)

        self.Image = Image

        class Fragment(db.Model):
            __tablename__ = "cms_fragment"
            id = db.Column(db.Integer(), primary_key=True)
            name = db.Column(db.String(), index=True)
            date_modified = db.Column(db.DateTime)
            content = db.Column(db.UnicodeText())

        self.Fragment = Fragment

        db.create_all()

    def get_page(self, path) -> typing.Optional[dataclasses.Page]:
        row = self.Page.query.filter_by(
            path=path
        ).first()
        if not row:
            return None
        return dataclasses.Page(
            path=row.path,
            title=row.title,
            nav_title=row.nav_title,
            sort_order=row.sort_order,
            content=row.content,
            date_modified=row.date_modified
        )

    def get_all_pages(self) -> typing.Iterable[dataclasses.StrippedPage]:
        for row in self.db.session.execute(self.db.select(
                self.Page.title,
                self.Page.path,
                self.Page.nav_title,
                self.Page.sort_order,
                self.Page.date_modified
        ).order_by(
            self.Page.path
        )):
            yield dataclasses.StrippedPage(
                title=row.title,
                path=row.path,
                nav_title=row.nav_title,
                sort_order=row.sort_order,
                date_modified=row.date_modified
            )

    def save_page(self, post: dataclasses.Page):
        result = self.db.session.execute(
            self.db.update(
                self.Page
            ).where(
                self.Page.path == post.path
            ).values(
                path=post.path,
                title=post.title,
                nav_title=post.nav_title,
                sort_order=post.sort_order,
                content=post.content,
                date_modified=post.date_modified
            )
        )
        if not result.rowcount:
            self.db.session.execute(
                self.db.insert(
                    self.Page
                ).values(
                    path=post.path,
                    title=post.title,
                    nav_title=post.nav_title,
                    sort_order=post.sort_order,
                    content=post.content,
                    date_modified=post.date_modified
                )
            )

        self.db.session.commit()

    def delete_page(self, path):
        self.db.session.execute(
            self.db.delete(self.Page).where(
                self.Page.path == path
            )
        )
        self.db.session.commit()

    def delete_image(self, filename):
        self.db.session.execute(
            self.db.delete(self.Image).where(
                self.Image.file == filename
            )
        )
        self.db.session.commit()

    def get_image(self, file):
        return self.Image.query.where(
            file == file
        ).first()

    def get_all_images(self) -> typing.Iterable[dataclasses.Image]:
        for image in self.db.session.execute(
                self.db.select(
                    self.Image
                )
        ):
            yield dataclasses.Image(
                file=image.Image.file,
                page=image.Image.page,
                size=image.Image.size,
                mime_type=image.Image.mime_type

            )

    def get_images_for_page(self, path) -> typing.Iterable[dataclasses.Image]:
        for image in self.Image.query.where(
                self.Image.page == path
        ):
            yield dataclasses.Image(
                file=image.file,
                page=image.page,
                size=image.size,
                mime_type=image.mime_type
            )

    def save_image(self, image: dataclasses.Image):
        self.db.session.execute(
            self.db.insert(
                self.Image
            ).values(
                **image.dict()
            )
        )
        self.db.session.commit()

    def get_nrof_pages(self) -> int:
        return self.db.session.execute(
            self.db.func.count(
                self.Page.id
            )
        ).scalar()

    def get_nrof_images(self) -> int:
        return self.db.session.execute(
            self.db.func.count(
                self.Image.id
            )
        ).scalar()

    def get_fragment(self, name: str) -> typing.Optional[dataclasses.Fragment]:
        fragment = self.db.session.execute(
            self.db.select(
                self.Fragment
            ).filter(
                self.Fragment.name == name
            )
        ).first()
        if fragment is None:
            return fragment
        return dataclasses.Fragment(
            name=fragment.Fragment.name,
            content=fragment.Fragment.content,
            date_modified=fragment.Fragment.date_modified
        )

    def save_fragment(self, fragment: dataclasses.Fragment) -> None:
        result = self.db.session.execute(
            self.db.update(
                self.Fragment
            ).where(
                self.Fragment.name == fragment.name
            ).values(
                content=fragment.content,
                date_modified=fragment.date_modified
            )
        )
        if not result.rowcount:
            self.db.session.execute(
                self.db.insert(
                    self.Fragment
                ).values(
                    name=fragment.name,
                    content=fragment.content,
                    date_modified=fragment.date_modified,
                )
            )

        self.db.session.commit()

    def get_all_fragments(self) -> typing.Iterable[dataclasses.StrippedFragment]:
        for fragment in self.db.session.query(
                self.db.select(
                    self.Fragment.name,
                    self.Fragment.date_modified
                )
        ):
            yield dataclasses.Fragment(
                name=fragment.name,
                date_modified=fragment.date_modified
            )
