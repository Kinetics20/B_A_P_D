class Ingredient:
    def __init__(self, name, protein, carbohydrates, fats):
        self.name = name
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fats = fats


class Meal:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient, amount):
        self.ingredients.append({'ingredient': ingredient, 'amount': amount})


class PlanDay:
    def __init__(self, name):
        self.name = name
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def summary(self):
        print(f'{self.name}\n')
        total_protein = 0
        total_carbohydrates = 0
        total_fats = 0
        total_kcal = 0

        for meal in self.meals:
            print(f'Meal : {meal.name}')
            meal_protein = 0
            meal_carbohydrates = 0
            meal_fats = 0
            meal_kcal = 0

            for ingredient_info in meal.ingredients:
                ingredient = ingredient_info['ingredient']
                amount = ingredient_info['amount']

                ingredient_protein = (ingredient.protein / 100) * amount
                ingredient_carbohydrates = (ingredient.carbohydrates / 100) * amount
                ingredient_fats = (ingredient.fats / 100) * amount
                ingredient_kcal = ingredient_protein * 4 + ingredient_carbohydrates * 4 + ingredient_fats * 9.4

                meal_protein += ingredient_protein
                meal_carbohydrates += ingredient_carbohydrates
                meal_fats += ingredient_fats
                meal_kcal += ingredient_kcal

                print(
                    f'- {amount}g {ingredient.name} ({ingredient_protein:.2f}g protein, {ingredient_carbohydrates:.2f}g carbohydrates {ingredient_fats:.2f}g fats, {ingredient_kcal:.1f} kcal)')
            print(f'Total: {total_protein:.2f}g protein, {total_carbohydrates:.2f}g carbohydrates, {total_fats:.2f}g fats, {total_kcal:.0f} kcal')
