from django.db import models

class FoodItem(models.Model):
    """Represents a food item with its calorie count."""
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"