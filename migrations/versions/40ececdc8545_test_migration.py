"""test Migration

Revision ID: 40ececdc8545
Revises: 0af1df1e742c
Create Date: 2018-11-21 08:35:09.320171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40ececdc8545'
down_revision = '0af1df1e742c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('pitch_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('text', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('pitch_id')
    )
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_secure')
    op.drop_table('pitches')
    # ### end Alembic commands ###
