"""auto-vote

Revision ID: 93f32d51bab4
Revises: 0c40c76fc42e
Create Date: 2024-10-10 13:07:24.904603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93f32d51bab4'
down_revision: Union[str, None] = '0c40c76fc42e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CaSCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # op.add_column('posts', sa.Column('created_id', sa.Integer(), nullable=False))
    # op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)
    # op.drop_constraint('posts_users_fk', 'posts', type_='foreignkey')
    # op.create_foreign_key(None, 'posts', 'users', ['created_id'], ['id'], ondelete='CASCADE')
    # op.drop_column('posts', 'owner_id')
    # op.add_column('users', sa.Column('name', sa.String(), nullable=False))
    # op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_index(op.f('ix_users_id'), table_name='users')
    # op.drop_column('users', 'name')
    # op.add_column('posts', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    # op.drop_constraint(None, 'posts', type_='foreignkey')
    # op.create_foreign_key('posts_users_fk', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    # op.drop_index(op.f('ix_posts_id'), table_name='posts')
    # op.drop_column('posts', 'created_id')
    op.drop_table('votes')
    # ### end Alembic commands ###
