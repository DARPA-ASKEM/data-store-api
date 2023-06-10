"""Update project asset with string id

Revision ID: 895deab7e80c
Revises: 5f6fd77df888
Create Date: 2023-06-09 21:20:24.369477

"""
import sqlalchemy as sa

# pylint: disable=no-member, invalid-name
from alembic import op

# revision identifiers, used by Alembic.
revision = "895deab7e80c"
down_revision = "0c372ef781b7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        table_name="project_asset",
        column_name="resource_id",
        nullable=False,
        type_=sa.String(),
    )


def downgrade() -> None:
    op.alter_column(
        table_name="project_asset",
        column_name="resource_id",
        nullable=False,
        type_=sa.Integer(),
    )