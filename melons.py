"""Classes for melon orders."""

class AbstractMelonOrder():
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
    
    def get_total(self):
        base_price = 5

        if self.species == "christmas":
            base_price = base_price + (1.5 * base_price)
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total = total + 3
    
        return round(total, 2)

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
    def __init__(self,species,qty,ctry):
        super().__init__(species,qty)
        self.country = ctry

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0.0
    passed_inspection = False
    order_type = "government" 
    def mark_inspection(self, passed):
        passed_inspection = passed