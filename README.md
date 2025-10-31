# Valuation Workflow Orchestrator

## Project Overview 🎯

The Valuation Workflow Orchestrator is a sophisticated full-stack application designed to simulate an AI-powered business valuation workflow. Built with React (frontend) and Django (backend), this application provides a streamlined process for business valuations through a modular, step-by-step approach.

### Key Features 🌟

- **Modular Workflow Pipeline**: Sequential processing from data input to final report
- **Real-time Validation**: Comprehensive input validation and error handling
- **Industry-specific Valuations**: Custom multipliers for different business sectors
- **Interactive UI**: Clean, responsive interface with real-time feedback
- **Detailed Reporting**: Comprehensive valuation reports with confidence scores

## Technical Stack 🛠

### Backend
- **Framework**: Django 5.0+
- **API**: Django REST Framework
- **Database**: SQLite
- **Additional Packages**: 
  - django-cors-headers
  - python-dotenv

### Frontend
- **Framework**: React 18+
- **HTTP Client**: Axios
- **State Management**: React Hooks
- **UI Components**: Custom components with modular CSS

## Project Structure 📁

```
EXITUITY_ASSESSMENT/
│
├── backend/                 # Django REST API
│   ├── manage.py           # Django management script
│   ├── requirements.txt    # Python dependencies
│   └── orchestrator/
│       ├── settings.py     # Django configuration
│       ├── urls.py         # API routing
│       ├── views.py        # Request handlers
│       ├── serializers.py  # Data validation
│       ├── steps/          # Pipeline modules
│       │   ├── input_step.py
│       │   ├── validation_step.py
│       │   ├── valuation_step.py
│       │   └── output_step.py
│       └── utils/
│           └── logger.py   # Logging configuration
│
└── frontend/               # React Frontend
    ├── package.json        # Node.js dependencies
    └── src/
        ├── App.js         # Main application
        ├── components/     # React components
        │   ├── ValuationForm.js
        │   └── ResultDisplay.js
        └── services/
            └── api.js     # API integration
```

## Installation Guide 🚀

### Backend Setup

1. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Unix/macOS
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start Development Server**
   ```bash
   python manage.py runserver
   ```
   Server will run at http://localhost:8000

### Frontend Setup

1. **Install Dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Start Development Server**
   ```bash
   npm start
   ```
   Application will run at http://localhost:3000

## API Documentation 📚

### Valuation Endpoint

**POST** `/api/run-valuation/`

Request Body:
```json
{
  "revenue": 1000000,      // Annual revenue
  "expenses": 750000,      // Annual expenses
  "growth_rate": 15,       // Growth rate percentage
  "industry": "technology" // Industry sector
}
```

Success Response:
```json
{
  "status": "Success",
  "logs": [
    "Input received",
    "Validation passed",
    "Valuation completed",
    "Report generated"
  ],
  "result": {
    "business_value": 750000,
    "confidence_score": 0.9,
    "analysis": {
      "profitability": {
        "net_income": 250000,
        "assessment": "Positive"
      },
      "growth_potential": 1.15,
      "industry_factor": 10
    }
  },
  "timestamp": "2025-10-30T12:45:00"
}
```

## Valuation Model 📊

The application uses a simplified yet effective valuation model:

```
Business Value = (Revenue - Expenses) × Industry Multiplier × (1 + Growth Rate)
```

### Industry Multipliers
| Industry      | Multiplier |
|---------------|------------|
| Technology    | 10x        |
| Healthcare    | 8x         |
| Manufacturing | 7x         |
| Services      | 6x         |
| Retail        | 5x        |
| Others        | 5x         |

## Pipeline Workflow Steps 🔄

1. **Data Input** 📥
   - Data type validation
   - Input sanitization
   - Format standardization

2. **Validation** ✔️
   - Negative value checks
   - Growth rate range validation (-100% to 1000%)
   - Revenue-expense ratio validation

3. **Valuation** 💹
   - Industry multiplier application
   - Growth rate factoring
   - Confidence score calculation

4. **Output Generation** 📋
   - Results formatting
   - Analysis compilation
   - Log aggregation

## Future Enhancements 🚀

1. **AI Integration**
   - Machine learning valuation models
   - Predictive growth analytics
   - Market trend analysis

2. **Enhanced Validation**
   - Industry-specific rules
   - Historical data validation
   - Market comparison checks

3. **Extended Reporting**
   - PDF report generation
   - Interactive charts and graphs
   - Comparative industry analysis

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors 👥

- Kunal Tyagi (@kunaltyagi760)

## Acknowledgments 🙏

- Exituity team for the project requirements and guidance
- Contributors who participate in improving this project