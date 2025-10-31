import React, { useState } from 'react';
import { runValuation } from '../services/api';

const ValuationForm = ({ setResult, setLoading, setError }) => {
  const [formData, setFormData] = useState({
    revenue: '',
    expenses: '',
    growth_rate: '',
    industry: 'technology'
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await runValuation({
        revenue: parseFloat(formData.revenue),
        expenses: parseFloat(formData.expenses),
        growth_rate: parseFloat(formData.growth_rate),
        industry: formData.industry
      });
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data || { message: 'An error occurred' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="revenue">Revenue ($)</label>
          <input
            type="number"
            id="revenue"
            name="revenue"
            value={formData.revenue}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="expenses">Expenses ($)</label>
          <input
            type="number"
            id="expenses"
            name="expenses"
            value={formData.expenses}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="growth_rate">Growth Rate (%)</label>
          <input
            type="number"
            id="growth_rate"
            name="growth_rate"
            value={formData.growth_rate}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="industry">Industry</label>
          <select
            id="industry"
            name="industry"
            value={formData.industry}
            onChange={handleChange}
            required
          >
            <option value="technology">Technology</option>
            <option value="retail">Retail</option>
            <option value="manufacturing">Manufacturing</option>
            <option value="services">Services</option>
            <option value="healthcare">Healthcare</option>
          </select>
        </div>

        <button type="submit">Run Valuation</button>
      </form>
    </div>
  );
};

export default ValuationForm;