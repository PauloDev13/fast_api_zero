from sqlalchemy import select

from fast_api_zero.models import User


def test_create_user(session):
    new_user = User(
        username='paulo', email='prmorais@gmail.com', password='1234'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'paulo'))

    assert user.username == 'paulo'
