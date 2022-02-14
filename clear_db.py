#清除資料庫資料用

from db_wrapper import DbWrapper


if __name__ == '__main__':
    db = DbWrapper()
    db.clear_db()