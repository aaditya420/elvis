# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'LINKS'
# The error was: 'NoneType' object is not subscriptable
# Unable to inspect table 'LINKS_QUORA'
# The error was: 'NoneType' object is not subscriptable
# Unable to inspect table 'LINKS_STACK'
# The error was: 'NoneType' object is not subscriptable
# Unable to inspect table 'LINKS_STACK_QUESTIONS'
# The error was: 'NoneType' object is not subscriptable

class LINKS(models.Model):
    _id = models.TextField(primary_key=True)  
    tag_name = models.TextField()
    tag_link = models.TextField()
    page_num = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'LINKS_STACK'

    def __str__(self):
        return self._id
