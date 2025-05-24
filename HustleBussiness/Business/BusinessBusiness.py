from HustleDatabase.Model.Business.BusinessModel import BusinessModel as Business

class BusinessBusiness():
    def __init__(self) -> None:
        pass

    def CalculatePrice(self, business):
        ingredient = sum(business.ingredient) + business.expectedProfit
        return ingredient