import React, { useState } from 'react';
import ValuationForm from './components/ValuationForm';
import ResultDisplay from './components/ResultDisplay';
import './App.css';

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Valuation Workflow Orchestrator</h1>
      </header>
      <main>
        <ValuationForm
          setResult={setResult}
          setLoading={setLoading}
          setError={setError}
        />
        <ResultDisplay
          result={result}
          loading={loading}
          error={error}
        />
      </main>
    </div>
  );
}

export default App;