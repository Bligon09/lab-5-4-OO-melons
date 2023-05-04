"""Classes for melon orders."""


class AbstractMelonOrder:


    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5 
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
    
     