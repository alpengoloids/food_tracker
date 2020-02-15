from django.db import models


# Create your models here.

class Food(models.Model):
    name = models.CharField(verbose_name="Food Name", max_length=200)
    calories = models.FloatField(verbose_name="Calories (kcal)")
    total_fats = models.FloatField(verbose_name="Total Fat (g)")
    saturated_fat = models.FloatField(verbose_name="Saturated Fat (g)")
    cholesterol = models.FloatField(verbose_name="Cholesterol (mg)")
    sodium = models.FloatField(verbose_name="Sodium (mg)")
    total_carbohydrates = models.FloatField(verbose_name="Total_Carbohydrates (mg)")
    dietary_fibre = models.FloatField(verbose_name="Dietary Fibre (mg)")
    sugar = models.FloatField(verbose_name="Sugar (g)")
    protein = models.FloatField(verbose_name="Protein (g)")

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Food"


class Meal(models.Model):
    BREAKFAST = 1
    MORNING_SNACKS = 2
    LUNCH = 3
    AFTERNOON_SNACKS = 4
    DINNER = 5
    EVENING_SNACKS = 6

    MEAL_TIME_TYPE = (
        (BREAKFAST, "Breakfast"),
        (MORNING_SNACKS, "Morning Snacks"),
        (LUNCH, "Lunch"),
        (DINNER, "Dinner"),
        (AFTERNOON_SNACKS, "Afternoon Snacks"),
        (EVENING_SNACKS, "Evening Snacks"),

    )
    food = models.ForeignKey(Food, verbose_name="Food", on_delete=models.CASCADE)
    serving_size = models.IntegerField(verbose_name="Serving Size")
    meal_time = models.IntegerField(verbose_name="Meal Time", choices=MEAL_TIME_TYPE)

    def __str__(self):
        return "%s" % self.food

    def get_total_calories(self):
        return self.serving_size * self.food.calories

    def get_total_fats(self):
        return self.serving_size * self.food.total_fats

    def get_saturated_fats(self):
        return self.serving_size * self.food.saturated_fat

    def get_total_cholesterol(self):
        return self.serving_size * self.food.cholesterol

    def get_total_sodium(self):
        return self.serving_size * self.food.sodium

    def get_total_carbohydrates(self):
        return self.serving_size * self.food.total_carbohydrates

    def get_total_dietary_fiber(self):
        return self.serving_size * self.food.dietary_fibre

    def get_total_sugar(self):
        return self.serving_size * self.food.sugar

    def get_protein(self):
        return self.serving_size * self.food.protein
