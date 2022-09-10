"""empty message

Revision ID: 76fad6fd5b87
Revises: 84e0c5398087
Create Date: 2022-09-09 15:55:06.600462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76fad6fd5b87'
down_revision = '84e0c5398087'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
