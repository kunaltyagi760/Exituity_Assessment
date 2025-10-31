def process_input(data):
    """Process and clean input data."""
    return {
        'revenue': float(data['revenue']),
        'expenses': float(data['expenses']),
        'growth_rate': float(data['growth_rate']),
        'industry': data['industry'].strip()
    }