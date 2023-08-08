"""Init db

Revision ID: 1f5853959c65
Revises:
Create Date: 2023-02-22 14:12:14.238575

"""
# pylint: disable=no-member, invalid-name
import os

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

from migrate.scripts.enums import (
    drop_enums,
    extracted_type,
    ontological_field,
    provenance_type,
    relation_type,
    resource_type,
    role,
    taggable_type,
    value_type,
)

# revision identifiers, used by Alembic.
revision = "1f5853959c65"
down_revision = None
branch_labels = None
depends_on = None

now_text = os.getenv("SQL_NOW_STATEMENT", "now()")


def upgrade() -> None:
    """
    Initialize tables as they were in v0.3.8
    """

    op.create_table(
        "active_concept",
        sa.Column("curie", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("curie"),
    )
    op.create_table(
        "model_framework",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("version", sa.String(), nullable=False),
        sa.Column("semantics", sa.String(), nullable=False),
        sa.Column("schema_url", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("name"),
    )
    op.create_table(
        "person",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("org", sa.String(), nullable=True),
        sa.Column("website", sa.String(), nullable=True),
        sa.Column("is_registered", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "project",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column(
            "timestamp",
            sa.DateTime(),
            server_default=sa.text(f"{now_text}"),
            nullable=True,
        ),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.Column("username", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "publication",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("xdd_uri", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "software",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "timestamp",
            sa.DateTime(),
            server_default=sa.text(f"{now_text}"),
            nullable=False,
        ),
        sa.Column("source", sa.String(), nullable=False),
        sa.Column("storage_uri", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("person_id", sa.Integer(), nullable=False),
        sa.Column("resource_id", sa.Integer(), nullable=False),
        sa.Column(
            "resource_type",
            resource_type,
            nullable=True,
        ),
        sa.Column(
            "role",
            role,
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["person_id"],
            ["person.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "extraction",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("publication_id", sa.Integer(), nullable=False),
        sa.Column(
            "type",
            extracted_type,
            nullable=False,
        ),
        sa.Column("data", sa.LargeBinary(), nullable=False),
        sa.Column("img", sa.LargeBinary(), nullable=False),
        sa.ForeignKeyConstraint(
            ["publication_id"],
            ["publication.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "model_runtime",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "timestamp",
            sa.DateTime(),
            server_default=sa.text(f"{now_text}"),
            nullable=False,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("left", sa.String(), nullable=False),
        sa.Column("right", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["left"],
            ["model_framework.name"],
        ),
        sa.ForeignKeyConstraint(
            ["right"],
            ["model_framework.name"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "ontology_concept",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("curie", sa.String(), nullable=False),
        sa.Column(
            "type",
            taggable_type,
            nullable=False,
        ),
        sa.Column("object_id", sa.Integer(), nullable=False),
        sa.Column("status", ontological_field, nullable=False),
        sa.ForeignKeyConstraint(
            ["curie"],
            ["active_concept.curie"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "project_asset",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("resource_id", sa.Integer(), nullable=False),
        sa.Column(
            "resource_type",
            resource_type,
            nullable=False,
        ),
        sa.Column("external_ref", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["project.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "provenance",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "timestamp",
            sa.DateTime(),
            server_default=sa.text(f"{now_text}"),
            nullable=False,
        ),
        sa.Column(
            "relation_type",
            relation_type,
            nullable=False,
        ),
        sa.Column("left", sa.Integer(), nullable=False),
        sa.Column(
            "left_type",
            provenance_type,
            nullable=False,
        ),
        sa.Column("right", sa.Integer(), nullable=False),
        sa.Column(
            "right_type",
            provenance_type,
            nullable=False,
        ),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("concept", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["person.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "feature",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("dataset_id", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("display_name", sa.String(), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "value_type",
            value_type,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "qualifier",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("dataset_id", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "value_type",
            value_type,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "qualifier_xref",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("qualifier_id", sa.Integer(), nullable=False),
        sa.Column("feature_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["feature_id"],
            ["feature.id"],
        ),
        sa.ForeignKeyConstraint(
            ["qualifier_id"],
            ["qualifier.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """
    Drop all tables and enums (LOSSY)
    """
    op.drop_table("qualifier_xref")
    op.drop_table("qualifier")
    op.drop_table("feature")
    op.drop_table("provenance")
    op.drop_table("project_asset")
    op.drop_table("ontology_concept")
    op.drop_table("model_runtime")
    op.drop_table("extraction")
    op.drop_table("association")
    op.drop_table("software")
    op.drop_table("publication")
    op.drop_table("project")
    op.drop_table("person")
    op.drop_table("model_framework")
    op.drop_table("active_concept")
    new_enums = iter(
        (
            resource_type,
            extracted_type,
            taggable_type,
            role,
            ontological_field,
            resource_type,
            relation_type,
            provenance_type,
            value_type,
        )
    )
    drop_enums(new_enums)
