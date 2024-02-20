import unittest
from datetime import datetime, timedelta
from article import Article, Panier

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.expiration_date = datetime.now() + timedelta(days=30)
        self.article = Article("Pomme", 2.5, 10, self.expiration_date)

    def test_price_positive(self):
        with self.assertRaises(ValueError):
            article = Article("Pomme", -2.5, 10, datetime.now() + timedelta(days=30))

    def test_add_quantity(self):
        self.article.add_quantity(5)
        self.assertEqual(self.article.quantity, 15)

    def test_remove_quantity(self):
        self.article.remove_quantity(3)
        self.assertEqual(self.article.quantity, 7)

    def test_remove_quantity_negative(self):
        with self.assertRaises(ValueError):
            self.article.remove_quantity(15)

    def test_is_expired(self):
        self.assertFalse(self.article.is_expired())

class TestPanier(unittest.TestCase):
    def setUp(self):
        self.panier = Panier()
        self.article1 = Article("Pomme", 2.5, 10, datetime.now() + timedelta(days=30))
        self.article2 = Article("Banane", 1.5, 20, datetime.now() + timedelta(days=20))

    def test_add_article(self):
        self.panier.add_article(self.article1)
        self.assertEqual(len(self.panier.articles), 1)

    def test_remove_article(self):
        self.panier.add_article(self.article1)
        self.panier.remove_article(self.article1)
        self.assertEqual(len(self.panier.articles), 0)

    def test_get_stock(self):
        self.panier.add_article(self.article1)
        self.panier.add_article(self.article2)
        self.assertEqual(self.panier.get_stock(), 30)

    def test_get_evolution(self):
        self.panier.add_article(self.article1)
        self.panier.add_article(self.article2)
        start_date = datetime.now() + timedelta(days=10)
        end_date = datetime.now() + timedelta(days=40)
        evolution = self.panier.get_evolution(start_date, end_date)
        self.assertEqual(evolution, {"Pomme": 10, "Banane": 20})
    def test_remise_not_less_than_zero(self):
        with self.assertRaises(ValueError):
            article = Article("Pomme", 2.5, 10, datetime.now() + timedelta(days=30), -10)
    def test_remise_not_less_than_100(self):
        with self.assertRaises(ValueError):
            article = Article("Pomme", 2.5, 10, datetime.now() + timedelta(days=30), 101)
    def test_prix_apres_remise(self):
        article = Article("Pomme", 2.5, 10, datetime.now() + timedelta(days=30), 20)
        self.assertEqual(article.price, 2.5)
        article.prix_apres_remise()
        self.assertEqual(article.price, 2.0)





if __name__ == '__main__':
    unittest.main()
