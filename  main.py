class ROICalculator:
    def __init__(self, income, expenses, down_payment_cost, monthly_costs):
        self.income = income
        self.expenses = expenses
        self.down_payment_cost = down_payment_cost
        self.monthly_costs = monthly_costs

    def calculate_cashflow(self):
        return self.income - self.expenses - self.monthly_costs

    def calculate_roi(self):
        cashflow = self.calculate_cashflow()
        total_investment = self.down_payment_cost + (self.monthly_costs * 12)  # Assume annual monthly costs
        return (cashflow / total_investment) * 100

# Example 
income = 50000  # Annual income
expenses = 30000  # Annual expenses
down_payment_cost = 100000  # One-time down payment cost
monthly_costs = 1000  # Monthly costs

roi_calculator = ROICalculator(income, expenses, down_payment_cost, monthly_costs)

cashflow = roi_calculator.calculate_cashflow()
roi = roi_calculator.calculate_roi()

print(f"Cash Flow: ${cashflow} per year")
print(f"ROI: {roi:.2f}%")