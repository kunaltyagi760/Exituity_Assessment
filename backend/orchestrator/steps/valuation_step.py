def calculate_valuation(data):
    """Calculate business valuation using a simple model."""
    # Simple valuation model:
    # Base valuation = (Revenue - Expenses) * Industry Multiplier * (1 + Growth Rate)
    
    industry_multipliers = {
        'technology': 10,
        'retail': 5,
        'manufacturing': 7,
        'services': 6,
        'healthcare': 8,
        'default': 5
    }
    
    net_income = data['revenue'] - data['expenses']
    industry = data['industry'].lower()
    multiplier = industry_multipliers.get(industry, industry_multipliers['default'])
    growth_factor = 1 + (data['growth_rate'] / 100)
    
    business_value = net_income * multiplier * growth_factor
    
    # Calculate confidence score based on factors
    confidence_factors = [
        0.3 if data['revenue'] > 0 else 0,  # Revenue factor
        0.3 if net_income > 0 else 0,  # Profitability factor
        0.2 if -20 <= data['growth_rate'] <= 100 else 0,  # Reasonable growth rate
        0.2 if industry in industry_multipliers else 0  # Known industry
    ]
    
    confidence_score = sum(confidence_factors)
    
    return {
        'business_value': round(business_value, 2),
        'confidence_score': round(confidence_score, 2),
        'factors': {
            'net_income': net_income,
            'industry_multiplier': multiplier,
            'growth_factor': growth_factor
        }
    }