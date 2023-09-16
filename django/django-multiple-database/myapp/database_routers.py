class MySQLRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'your_app_label':
            return 'mysql_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'your_app_label':
            return 'mysql_db'
        return None

class PostgresRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'your_app_label':
            return 'postgres_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'your_app_label':
            return 'postgres_db'
        return None
