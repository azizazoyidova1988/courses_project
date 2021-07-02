from django.db import connection
from contextlib import closing


def get_items():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from Items""")
        items = dict_fetchall(cursor)
        return items



def get_teams():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from About""")
        teams = dict_fetchall(cursor)
        return teams



def get_courses():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from Course""")
        courses = dict_fetchall(cursor)
        return courses


def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from News""")
        news = dict_fetchall(cursor)
        return news



def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))