import datetime
from random import randint, choice

from fastapi import APIRouter

from lesson_6.hw.db import users, products, orders, database

router = APIRouter()
# MIN_NUM = 10
# MAX_NUM = 100
MIN_PRICE = 1
MAX_PRICE = 10_000


@router.get("/fake_data/{count}")
async def create_note(count: int):
    """Добавление тестовых пользователей в БД"""
    for i in range(count):
        query = users.insert().values(firstname=f'firstname_{i}',
                                      lastname=f'lastname_{i}',
                                      email=f'mail{i}@m.t',
                                      password=f'password{i}')
        await database.execute(query)

    """Добавление тестовых товаров в БД"""
    for i in range(count):
        query = products.insert().values(title=f'title_{i}',
                                         description=f'description_{i}',
                                         price=randint(MIN_PRICE, MAX_PRICE))
        await database.execute(query)

    """Добавление тестовых заказов в БД"""
    for i in range(count):
        query = orders.insert().values(user_id=randint(1, count),
                                       prod_id=randint(1, count),
                                       date=datetime.date.today(),
                                       status=choice(['размещен', 'ожидает оплаты', 'оплачен', 'отправлен',
                                                      'доставляется', 'доставлен', 'выполнен', 'отменен']))
        await database.execute(query)

    return {'message': f'{count} fake users, {count} fake products'
                       f'and {count} fake orders created'}
