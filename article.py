from datetime import datetime, timedelta

class Article:
    def __init__(self, name, price, quantity, expiration_date):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date

    def add_quantity(self, quantity):
        self.quantity += quantity

    def remove_quantity(self, quantity):
        if self.quantity - quantity >= 0:
            self.quantity -= quantity
        else:
            raise ValueError("La quantité de produit ne peut pas être négative")

    def is_expired(self):
        return datetime.now() > self.expiration_date

    def __str__(self):
        return f"{self.name} - Prix: {self.price} € - Quantité: {self.quantity}"

class Panier:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def remove_article(self, article):
        self.articles.remove(article)

    def get_stock(self):
        return sum(article.quantity for article in self.articles)

    def print_stock(self):
        for article in self.articles:
            print(article)

    def get_evolution(self, start_date, end_date):
        evolution = {}
        for article in self.articles:
            if start_date <= article.expiration_date <= end_date:
                if article.name in evolution:
                    evolution[article.name] += article.quantity
                else:
                    evolution[article.name] = article.quantity
        return evolution
