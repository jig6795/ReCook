# Generated by Django 2.2.7 on 2021-03-31 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('similar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allergyfood',
            name='allergy',
        ),
        migrations.DeleteModel(
            name='AllergyGroup',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='FoodLike',
        ),
        migrations.DeleteModel(
            name='Fridge',
        ),
        migrations.DeleteModel(
            name='IngredientsBig',
        ),
        migrations.DeleteModel(
            name='IngredientsMiddle',
        ),
        migrations.DeleteModel(
            name='IngredientsSmall',
        ),
        migrations.RemoveField(
            model_name='recipehashtag',
            name='recipe',
        ),
        migrations.DeleteModel(
            name='RecipeIngredients',
        ),
        migrations.DeleteModel(
            name='RecipeLike',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Sequence',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='userhashtag',
            name='hashtag',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.DeleteModel(
            name='Allergy',
        ),
        migrations.DeleteModel(
            name='AllergyFood',
        ),
        migrations.DeleteModel(
            name='Hashtag',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.DeleteModel(
            name='RecipeHashtag',
        ),
        migrations.DeleteModel(
            name='UserHashtag',
        ),
    ]