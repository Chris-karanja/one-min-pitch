"""second migration

Revision ID: 42102e8e85de
Revises: bf8608e4d4cf
Create Date: 2018-11-19 11:01:36.476034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42102e8e85de'
down_revision = 'bf8608e4d4cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
