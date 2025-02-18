"""Add game_user Association Table

Revision ID: a266778c024f
Revises: 2cd09fadb051
Create Date: 2023-08-30 13:48:28.945564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a266778c024f'
down_revision = '2cd09fadb051'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_users',
    sa.Column('game_id', sa.Integer(), nullable=True, primar_key=True),
    sa.Column('user_id', sa.Integer(), nullable=True, primar_key=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_game_users_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_game_users_user_id_users'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_users')
    # ### end Alembic commands ###
