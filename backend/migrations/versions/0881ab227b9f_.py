"""
Revision ID: 0881ab227b9f
Revises: 21659fcad438
Create Date: 2026-02-28 20:02:05.163134
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision: str = '0881ab227b9f'
down_revision: Union[str, Sequence[str], None] = '21659fcad438'
branch_labels = None
depends_on = None

# ✅ DEFINE ENUM ONCE
selection_status_enum = postgresql.ENUM(
    "PENDING",
    "ACCEPTED",
    "REJECTED",
    name="selection_status_enum"
)

def upgrade() -> None:
    # 1️⃣ CREATE ENUM TYPE FIRST
    selection_status_enum.create(op.get_bind(), checkfirst=True)

    # 2️⃣ ADD COLUMNS
    op.add_column(
        "resumes",
        sa.Column(
            "selection_status",
            selection_status_enum,
            nullable=False,
            server_default="PENDING"
        )
    )

    op.add_column(
        "resumes",
        sa.Column("review_note", sa.Text(), nullable=True)
    )

    # 3️⃣ CREATE INDEX
    op.create_index(
        op.f("ix_resumes_selection_status"),
        "resumes",
        ["selection_status"],
        unique=False
    )

def downgrade() -> None:
    op.drop_index(op.f("ix_resumes_selection_status"), table_name="resumes")
    op.drop_column("resumes", "review_note")
    op.drop_column("resumes", "selection_status")

    # 4️⃣ DROP ENUM TYPE
    selection_status_enum.drop(op.get_bind(), checkfirst=True)