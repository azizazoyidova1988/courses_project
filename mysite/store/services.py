from django.db import connection
from contextlib import closing


def get_items():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from items""")
        items = dict_fetchall(cursor)
        return items



def get_teams():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from team""")
        teams = dict_fetchall(cursor)
        return teams



def get_courses():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from course""")
        courses = dict_fetchall(cursor)
        return courses


def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from news""")
        news = dict_fetchall(cursor)
        return news

def get_news_by_id(news_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from news where news.id=%s""", [news_id])
        new = dict_fetchone(cursor)
        return new


def get_course_by_id(course_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from course where course.id=%s""", [course_id])
        course = dict_fetchall(cursor)
        return course


def get_video_by_course_id(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from video WHERE video.course_id = %s  """, [pk])
        video_course = dict_fetchall(cursor)
        return video_course

def get_commenter(pk,pks):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from commenter where commenter.course_id=%s and commenter.video_id=%s""",[pk,pks])
        commenter = dict_fetchall(cursor)
        return commenter


def get_commenter_by_limit():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  * from commenter order by created_at desc limit 3""" )
        comment = dict_fetchall(cursor)
        return comment


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