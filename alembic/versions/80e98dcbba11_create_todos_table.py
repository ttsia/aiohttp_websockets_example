"""create todos table

Revision ID: 80e98dcbba11
Revises: 
Create Date: 2020-02-20 08:55:08.793677

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime as dt

# revision identifiers, used by Alembic.
revision = "80e98dcbba11"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "todos",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.String(140)),
        sa.Column("timestamp", sa.DateTime, index=True, default=dt.utcnow),
    )


def downgrade():
    op.drop_table("todos")
