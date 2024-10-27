"""entries table

Revision ID: 8a48cd99eb4c
Revises: 0763c0f8478a
Create Date: 2024-05-18 17:09:23.305633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a48cd99eb4c'
down_revision = '0763c0f8478a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('purchase', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_purchase_owner_id'), 'purchase', ['owner_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_purchase_owner_id'), table_name='purchase')
    op.drop_column('purchase', 'owner_id')
    # ### end Alembic commands ###
