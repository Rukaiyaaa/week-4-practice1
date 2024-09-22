from django.db import models

class Practice(models.Model):
    auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    # file_field = models.FileField(upload_to='files/')
    # file_path_field = models.FilePathField(path='/path/to/files/')
    generic_ip_address_field = models.GenericIPAddressField()
    integer_field = models.IntegerField()   
    url_field = models.URLField()

    def __str__(self):
        return f"{self.date_field}"