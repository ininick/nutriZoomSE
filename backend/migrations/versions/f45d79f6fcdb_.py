"""empty message

Revision ID: f45d79f6fcdb
Revises: 680f137e6e56
Create Date: 2024-02-01 14:51:46.831818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f45d79f6fcdb'
down_revision = '680f137e6e56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nutritiondetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nutritionamount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nutritiondetails')
    # ### end Alembic commands ###
