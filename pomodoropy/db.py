



TASKS_SQL = """
    create table tasks(id integer primary key, name varchar, owner integer,
                       genre integer, year integer, rating integer)
    """
PROJECT_SQL = """
    create table books(id integer primary key, title varchar, author integer,
                       genre integer, year integer, rating integer)
    """

AUTHORS_SQL = """
    create table authors(id integer primary key, name varchar, birthdate text)
    """
GENRES_SQL = """
    create table genres(id integer primary key, name varchar)
    """
INSERT_AUTHOR_SQL = """
    insert into authors(name, birthdate) values(?, ?)
    """
INSERT_GENRE_SQL = """
    insert into genres(name) values(?)
    """
INSERT_BOOK_SQL = """
    insert into books(title, year, author, genre, rating)
                values(?, ?, ?, ?, ?)
    """
