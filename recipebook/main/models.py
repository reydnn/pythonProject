from django.db import models


class Ingredient(models.Model):
    """Ингредиент"""

    title = models.CharField('Название', max_length=50, null=False, default=None)
    type_product = models.CharField(' Вид', max_length=50, null=False, default=None)

    def __str__(self):
        return f'{self.title} ({self.type_product})'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Recipe(models.Model):
    """Рецепт"""

    title = models.CharField('Название', max_length=50, null=False, default=None)
    ingredients = models.ManyToManyField("Ingredient", verbose_name='Ингредиенты', related_name='recipe_ingredients')
    description = models.TextField("Описание")
    time_cook = models.IntegerField("Время приготовления (мин.)", null=False, default=None)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
