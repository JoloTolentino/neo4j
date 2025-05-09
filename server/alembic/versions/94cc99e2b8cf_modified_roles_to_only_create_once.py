"""modified roles to only create once

Revision ID: 94cc99e2b8cf
Revises: c7a8cb5bfcf2
Create Date: 2025-04-18 22:35:54.699738

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "94cc99e2b8cf"
down_revision: Union[str, None] = "c7a8cb5bfcf2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "transactions",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("table", sa.String(), nullable=False),
        sa.Column("transaction", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("uuid", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id", "uuid"),
    )
    op.create_table(
        "persons",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column(
            "role", sa.Enum("actor", "director", name="movie_roles"), nullable=False
        ),
        sa.Column("movie_id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("uuid", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["movie_id"],
            ["movies.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.drop_table("Persons")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "Persons",
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("age", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "role",
            postgresql.ENUM("actor", "director", name="roles"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("movie_id", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("uuid", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["movie_id"], ["movies.uuid"], name="Persons_movie_id_fkey"
        ),
        sa.PrimaryKeyConstraint("uuid", name="Persons_pkey"),
    )
    op.drop_table("persons")
    op.drop_table("transactions")
    # ### end Alembic commands ###
