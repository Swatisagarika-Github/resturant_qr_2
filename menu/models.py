from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    table_no = models.IntegerField()
    items = models.ManyToManyField(MenuItem)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"Table {self.table_no} - {self.timestamp}"