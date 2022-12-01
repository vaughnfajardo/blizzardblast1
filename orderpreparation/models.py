# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(primary_key=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return str(self.customer_name)



class Customization(models.Model):
    shake = models.OneToOneField('Milkshake', models.DO_NOTHING, primary_key=True)
    ingredient_name = models.ForeignKey('Ingredient', models.DO_NOTHING, db_column='ingredient_name', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    tx_num = models.ForeignKey('Orders', models.DO_NOTHING, db_column = 'tx_num', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customization'

    def __str__(self):
        return str(self.ingredient_name)



class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'
        


class Ingredient(models.Model):
    ingredient_name = models.CharField(primary_key=True, max_length=25)
    CATEGORY = [
        ('Nuts', 'Nuts'),
        ('Fruits', 'Fruits'),
        ('Chocolate', 'Chocolate'),
        ('Baked', 'Baked'), 
        ('Milk', 'Milk'),
        ('Mix-in', 'Mix-in'),
        ('Base', 'Base'),
        ('Topping','Topping')
    ]
    category = models.CharField(max_length=25, choices=CATEGORY, blank=True)
    quantity_on_hand = models.IntegerField(blank=True, null=True)
    price_per_serving = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredient'


    def __str__(self):
        return str(self.ingredient_name)


class Manager(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    manager_schedule = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'

    def __str__(self):
        return str(self.employee)



class Milkshake(models.Model):
    shake_id = models.IntegerField(primary_key=True)
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='order', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'milkshake'

    def __str__(self):
        return str(self.recipe)





class Orders(models.Model):
    txn_number = models.IntegerField(primary_key=True)
    order_date = models.DateField(blank=True, null=True)
    customer_name = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer_name', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'orders'

    def __str__(self):
        return str(self.txn_number)


class Recipe(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    recipe_name = models.CharField(max_length=25)
    SIZES = [
        ('8', '8'),
        ('12', '12'),
        ('16', '16'),
    ]
    sizes = models.CharField(max_length=10, blank=True, choices=SIZES, null=True)
    price = models.IntegerField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'recipe'

    def __str__(self):
        return f'{str(self.sizes)} {str(self.recipe_name)}'



class RecipeIngredient(models.Model):
    in_recip = models.IntegerField(primary_key=True)
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe_ingredient'

    def __str__(self):
        return f'Recipe: {str(self.recipe)} | Ingredient: {str(self.ingredient)}'


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    staff_role = models.CharField(max_length=25, blank=True, null=True)
    role_schedule = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'

    def __str__(self):
        return str(self.employee)
