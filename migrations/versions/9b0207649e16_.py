"""empty message

Revision ID: 9b0207649e16
Revises: 32b6fdd8d008
Create Date: 2020-07-18 01:47:14.907449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b0207649e16'
down_revision = '32b6fdd8d008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('brands', sa.Column('thumbnail_filename', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('brands', 'thumbnail_filename')
    # ### end Alembic commands ###
