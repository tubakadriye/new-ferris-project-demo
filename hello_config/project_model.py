from flask_appbuilder.models.mixins import AuditMixin
from flask_appbuilder.models.sqla import Model, Base
from sqlalchemy import Integer, String, Column, Table, Sequence, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import synonym
from sqlalchemy.ext.declarative import declarative_base

from ferrisapp.app.models.sqla import SoftDeleteMixin

from ferris_fab_vault.models.secret import Secret
# from ferris_fab_dashboard.models.chart import Chart


project_secrets = Table(
    "project_secrets",
    Model.metadata,
    Column("id", Integer, Sequence("project_secrets_id_seq"), primary_key=True),
    Column("project_id", Integer, ForeignKey("project.id")),
    Column("secret_id", Integer, ForeignKey("secret.id")),
    UniqueConstraint("project_id", "secret_id")
)

project_charts = Table(
     "project_charts",
     Model.metadata,
     Column("id", Integer, Sequence("project_charts_id_seq"), primary_key=True),
     Column("project_id", Integer, ForeignKey("project.id")),
     Column("chart_id", Integer, ForeignKey("chart.id")),
     UniqueConstraint("project_id", "chart_id")
)


class Project(Model, AuditMixin, SoftDeleteMixin):

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

     
    charts = relationship(
         "Chart", secondary=project_charts, backref="project", lazy="joined"
     )

    secrets = relationship(
        "Secret", secondary=project_secrets, backref="project", lazy="joined"
    )

    @property
    def users(self):
        return self.project_users

    def user_ids(self):
        return [u.id for u in self.users]

    def __repr__(self):
        return self.name

    def delete(self):
        for repository in self.repositories:
            repository.delete()

        for package in self.packages:
            package.delete()

        super().delete()

