def generate_output(valuation_result):
    """Generate final output with valuation results and insights."""
    output = {
        'business_value': valuation_result['business_value'],
        'confidence_score': valuation_result['confidence_score'],
        'analysis': {
            'profitability': {
                'net_income': valuation_result['factors']['net_income'],
                'assessment': 'Positive' if valuation_result['factors']['net_income'] > 0 else 'Negative'
            },
            'growth_potential': valuation_result['factors']['growth_factor'],
            'industry_factor': valuation_result['factors']['industry_multiplier']
        }
    }
    
    return output