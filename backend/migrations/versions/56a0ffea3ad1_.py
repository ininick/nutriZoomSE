"""empty message

Revision ID: 56a0ffea3ad1
Revises: bbd9e251b0e6
Create Date: 2024-02-15 16:27:36.878567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56a0ffea3ad1'
down_revision = 'bbd9e251b0e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('steps', sa.String(length=300), nullable=True),
    sa.Column('favorite_count', sa.Integer(), nullable=True),
    sa.Column('cooktime', sa.Integer(), nullable=True),
    sa.Column('portions', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('detail', sa.String(length=1000), nullable=True),
    sa.Column('author', sa.String(length=100), nullable=True),
    sa.Column('publishdate', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('favoriterecipe',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'recipe_id')
    )
    op.create_table('nutritiondetails',
    sa.Column('nutrition_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['nutrition_id'], ['nutritions.id'], ),
    sa.PrimaryKeyConstraint('nutrition_id', 'ingredient_id')
    )
    op.create_table('recipedetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.Column('ingredients_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('unit', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['ingredients_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipedetails')
    op.drop_table('nutritiondetails')
    op.drop_table('favoriterecipe')
    op.drop_table('article')
    op.drop_table('recipes')
    # ### end Alembic commands ###
