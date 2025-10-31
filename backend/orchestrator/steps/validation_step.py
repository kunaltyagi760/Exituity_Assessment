def validate_data(data):
    """Validate the input data."""
    errors = []
    
    # Check for negative values
    if data['revenue'] < 0:
        errors.append("Revenue cannot be negative")
    if data['expenses'] < 0:
        errors.append("Expenses cannot be negative")
        
    # Check growth rate range
    if not (-100 <= data['growth_rate'] <= 1000):
        errors.append("Growth rate must be between -100% and 1000%")
        
    # Check if expenses exceed revenue
    if data['expenses'] > data['revenue']:
        errors.append("Expenses cannot exceed revenue")
        
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }