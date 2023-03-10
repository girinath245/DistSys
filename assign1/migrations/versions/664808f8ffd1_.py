"""empty message

Revision ID: 664808f8ffd1
Revises: 
Create Date: 2023-01-26 18:58:31.932978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '664808f8ffd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('queue_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nxt_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(), nullable=True),
    sa.Column('start_ind', sa.Integer(), nullable=True),
    sa.Column('end_ind', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('consumer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('offset', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('producer')
    op.drop_table('consumer')
    op.drop_table('topics')
    op.drop_table('queue_db')
    # ### end Alembic commands ###
