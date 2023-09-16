from django.db import models

class MySQLModel(models.Model):
    # Fields
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'mysql_table'
        app_label = 'your_app_label'
        using = 'mysql_db'

class PostgresModel(models.Model):
    # Fields
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'postgres_table'
        app_label = 'your_app_label'
        using = 'postgres_db'
