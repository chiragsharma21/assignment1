# myapp/models.py

from djongo import models

class Scrap(models.Model):
    job_title = models.CharField(max_length=255)
    min_salary = models.CharField(max_length=20)
    max_salary = models.CharField(max_length=20)
    avg_salary = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    link = models.URLField()

    class Meta:
        db_table = 'scrap'  # Set the table name to match your existing MongoDB collection name

    def __str__(self):
        return self.job_title
