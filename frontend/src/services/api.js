import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

export const runValuation = (data) => {
  return axios.post(`${API_BASE_URL}/run-valuation/`, data);
};