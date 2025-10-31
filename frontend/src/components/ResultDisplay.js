import React from 'react';

const ResultDisplay = ({ result, loading, error }) => {
  if (loading) {
    return <div className="loading">Processing valuation...</div>;
  }

  if (error) {
    return (
      <div className="error">
        <h3>Error</h3>
        <p>{error.message || JSON.stringify(error)}</p>
        {error.errors && (
          <ul>
            {Object.entries(error.errors).map(([key, value]) => (
              <li key={key}>{`${key}: ${value}`}</li>
            ))}
          </ul>
        )}
      </div>
    );
  }

  if (!result) {
    return null;
  }

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      maximumFractionDigits: 0
    }).format(value);
  };

  return (
    <div className="results-container">
      <h2>Valuation Results</h2>
      <div>
        <h3>Business Value</h3>
        <p>{formatCurrency(result.result.business_value)}</p>
      </div>

      <div>
        <h3>Confidence Score</h3>
        <p>{(result.result.confidence_score * 100).toFixed(1)}%</p>
      </div>

      <div>
        <h3>Analysis</h3>
        <ul>
          <li>
            Profitability: {result.result.analysis.profitability.assessment}
            ({formatCurrency(result.result.analysis.profitability.net_income)})
          </li>
          <li>Growth Factor: {result.result.analysis.growth_potential.toFixed(2)}x</li>
          <li>Industry Multiplier: {result.result.analysis.industry_factor}x</li>
        </ul>
      </div>

      <div className="logs-container">
        <h3>Process Logs</h3>
        {result.logs.map((log, index) => (
          <div key={index} className="log-item">
            {log}
          </div>
        ))}
      </div>
    </div>
  );
};

export default ResultDisplay;