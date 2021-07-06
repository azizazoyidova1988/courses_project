from django.db import connection
from contextlib import closing


def get_courses():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from course""")
        courses = dict_fetchall(cursor)
        return courses


def get_courses_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(title) from course""")
        courses_count = dict_fetchall(cursor)
        return courses_count


def get_teams():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from team""")
        teams = dict_fetchall(cursor)
        return teams


def get_teams_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from team""")
        teams_count = dict_fetchall(cursor)
        return teams_count


def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from news""")
        news = dict_fetchall(cursor)
        return news


def get_news_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(title) from news""")
        news_count = dict_fetchall(cursor)
        return news_count


def get_commenter():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from commenter""")
        commenters = dict_fetchall(cursor)
        return commenters


def get_commenter_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from commenter""")
        customers_count = dict_fetchall(cursor)
        return customers_count

def get_items():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from items""")
        items = dict_fetchall(cursor)
        return items


def get_items_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(title) from items""")
        items_count = dict_fetchall(cursor)
        return items_count

def get_videos():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from video""")
        video = dict_fetchall(cursor)
        return video


def get_videos_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(title) from video""")
        videos_count = dict_fetchall(cursor)
        return videos_count

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
