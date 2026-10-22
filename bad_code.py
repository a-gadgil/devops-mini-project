# Simple function to compute profit based on revenue and cost

def compute_profit(revenue, cost):
    """
    Computes the profit by subtracting cost from revenue.

    Parameters:
    revenue (float): The total revenue generated.
    cost (float): The total cost incurred.

    Returns:
    float: The computed profit.
    """
    profit = revenue - cost
    return profit

# Example usage
if __name__ == "__main__":
    revenue = 1000.0
    cost = 750.0
    profit = compute_profit(revenue, cost)
    print(f"Profit: ${profit:.2f}")

    