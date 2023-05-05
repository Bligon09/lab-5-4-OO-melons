"""Classes for melon orders."""
from random import choice

class AbstractMelonOrder:
    # price_log = []

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        #self.price_log = []
        
    def get_based_price(self):
        
        #if list is full, reset
        # while True:
        splurge_price = choice(range(5, 10))
            # print (splurge_price)
            # if splurge_price not in price_log:
            #     price_log.append(splurge_price)
            #     print (price_log)
            #     break
            # else:
            #     continue

        return splurge_price 



    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_based_price()
        print(base_price)
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    
    def get_total_Christmas(self):
        """Calculate price, including tax."""

        base_price = 5 * 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total 

class GovernmentMelonOrder(AbstractMelonOrder):
       
    def __init__(self,species,qty):
        """Initialize melon order attributes."""

        self.order_type = "government"
        super().__init__(species, qty)
        self.passed_inspection = False

    def passed_inspection(self):
        """Record the fact than an order has been shipped."""

        self.passed_inspection = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self,species,qty):
        """Initialize melon order attributes."""

        self.order_type = "domestic"
        self.tax = 0.08
        super().__init__(species, qty)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17
        super().__init__(species, qty)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def int_holiday_shipping(self):

        total = super().get_total_Christmas()
        if int(self.qty) < 10:
            total += 3.00
            
        return total 
    
     