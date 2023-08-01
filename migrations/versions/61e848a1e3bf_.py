"""empty message

Revision ID: 61e848a1e3bf
Revises: 651b3c3c0ef7
Create Date: 2023-08-01 02:33:26.416233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61e848a1e3bf'
down_revision = '651b3c3c0ef7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('heigh', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('hair_color', sa.String(length=80), nullable=True),
    sa.Column('skin_color', sa.String(length=80), nullable=True),
    sa.Column('eye_color', sa.String(length=80), nullable=True),
    sa.Column('birth_year', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('people')
    # ### end Alembic commands ###