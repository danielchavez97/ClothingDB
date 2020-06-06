"""Added brand name

Revision ID: 4dad688de007
Revises: 980893b75ee8
Create Date: 2020-06-06 13:19:46.488529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dad688de007'
down_revision = '980893b75ee8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_column('item_metadata', 'field_edited')
    op.add_column('items', sa.Column('brand_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'brand_name')
    op.add_column('item_metadata', sa.Column('field_edited', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
