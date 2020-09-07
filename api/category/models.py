from django.db import models

# Create your models here.


class Category(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'MODELNAME'
        verbose_name_plural = 'MODELNAMEs'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.name
