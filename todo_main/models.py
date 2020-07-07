from django.db import models

# Create your models here.
class TbTodolist(models.Model):
    idnew_table = models.AutoField(primary_key=True)
    todo_title = models.CharField(max_length=300, blank=True, null=True)
    todo_date = models.DateTimeField(blank=True, null=True)
    todo_contents = models.CharField(max_length=1000, blank=True, null=True)

    def item_save(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'tb_todolist'
