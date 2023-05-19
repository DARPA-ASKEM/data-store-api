"""20230516154354

Revision ID: 0c372ef781b7
Revises: 2e9a3d2ffe83
Create Date: 2023-05-16 08:43:56.077919

"""
import sqlalchemy as sa

# pylint: disable=no-member, invalid-name
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "0c372ef781b7"
down_revision = "2e9a3d2ffe83"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        "provenance",
        "left",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.alter_column(
        "provenance",
        "right",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "provenance",
        "right",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column(
        "provenance",
        "left",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )