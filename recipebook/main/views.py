from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse


from main.models import Ingredient, Recipe


def home(request):
    """Главная страница. Редирект на `/recipes`"""

    response = redirect(reverse("recipes"))
    return response


def recipes(request):
    """Список рецептов с поиском по ингредиенту и рецепту"""

    try:
        recipe_id = int(request.GET.get("recipe_id"))
    except (ValueError, TypeError):
        recipe_id = None

    try:
        recipe_ingredient_id = int(request.GET.get("ingredient_id"))
    except (ValueError, TypeError):
        recipe_ingredient_id = None

    query = Q()
    if recipe_id:
        query.add(
            Q(pk=recipe_id), Q.AND,
        )
    if recipe_ingredient_id:
        query.add(
            Q(ingredients__pk=recipe_ingredient_id), Q.AND,
        )

    recipes_objects = Recipe.objects.prefetch_related("ingredients").filter(query)
    ingredients_lookup = Ingredient.objects.all()
    recipes_lookup = Recipe.objects.all()

    return render(
        request,
        "main/index.html",
        {
            "recipes": recipes_objects,
            "form": {
                "ingredient": {
                    "title": "Ингредиент",
                    "objects": ingredients_lookup,
                    "selected": recipe_ingredient_id,
                },
                "recipe": {
                    "title": "Название",
                    "objects": recipes_lookup,
                    "selected": recipe_id,
                },
            },
        },
    )