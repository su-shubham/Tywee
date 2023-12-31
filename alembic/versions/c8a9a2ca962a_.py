"""empty message

Revision ID: c8a9a2ca962a
Revises: 1927c158602e
Create Date: 2023-07-25 22:52:15.362152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8a9a2ca962a'
down_revision = '1927c158602e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.Column('order_amount', sa.Float(), nullable=True),
    sa.Column('order_status', sa.String(), nullable=True),
    sa.Column('shipping_address', sa.Text(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_details',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('created', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_details')
    op.drop_table('order')
    # ### end Alembic commands ###
