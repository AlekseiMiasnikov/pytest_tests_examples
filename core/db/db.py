from peewee import PostgresqlDatabase, Model, MySQLDatabase, SqliteDatabase
from core.helpers import get_settings


class DB:
    def connection(self, environment='test'):
        data = get_settings(environment)
        engine = None

        if data['DB']['DB_TYPE'].lower() == 'postgresql':
            engine = PostgresqlDatabase(
                database=data['DB']['DB_NAME'],
                user=data['DB']['USER'],
                password=data['DB']['PASSWORD'],
                host=data['DB']['PORT'],
                port=int(data['DB']['PORT'])
            )
        elif data['DB']['DB_TYPE'].lower() == 'mysql':
            engine = MySQLDatabase(
                database=data['DB']['DB_NAME'],
                user=data['DB']['USER'],
                password=data['DB']['PASSWORD'],
                host=data['DB']['HOST'],
                port=int(data['DB']['PORT'])
            )
        elif data['DB']['DB_TYPE'].lower() == 'sqlite':
            engine = SqliteDatabase(
                database=data['DB']['PATH'],
                pragmas={
                    'journal_mode': 'wal',
                    'cache_size': -1024 * 64
                }
            )

        return engine


class BaseModel(Model):
    class Meta:
        database = DB().connection()
