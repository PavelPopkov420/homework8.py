class Soup:
    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None


    def show_my_soup(self):
        if self.ingredient:
            print(f'Суп - {self.ingredient}')
        else:
            print('Обычный кипяток')

soup1 = Soup('Капуста')
soup2 = Soup('Мясо')
soup3 = Soup(5)
soup1.show_my_soup()
soup2.show_my_soup()
soup3.show_my_soup()

