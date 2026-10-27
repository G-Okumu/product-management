"""add product price check constraint

Revision ID: 67e04b3d4a78
Revises: ce3320f5e922
Create Date: 2026-10-27 10:47:49.439651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67e04b3d4a78'
down_revision = 'ce3320f5e922'
branch_labels = None
depends_on = None



def upgrade():
    op.create_check_constraint(
        "product_price_must_be_greater_than_one",
        "products",
        "price >= 1"
    )

def downgrade():
    op.drop_constraint(
        "product_price_must_be_greater_than_one",
        "products",
        type_="check"
    )
