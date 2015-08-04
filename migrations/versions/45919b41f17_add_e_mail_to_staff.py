"""Add E-Mail to staff

Revision ID: 45919b41f17
Revises: None
Create Date: 2015-07-27 15:17:42.263722

"""

# revision identifiers, used by Alembic.
revision = '45919b41f17'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('staff', sa.Column('email', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_staff_email'), 'staff', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_staff_email'), table_name='staff')
    op.drop_column('staff', 'email')
    ### end Alembic commands ###
