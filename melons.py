"""Classes for melon orders."""

class AbstractMelonOrder():
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = None
    
    def get_total(self):
        
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
    
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17
    def __init__(self,species,qty,country):
        self.country = country  
        self.species = species  
        self.qty = qty

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
