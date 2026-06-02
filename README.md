# Sacred Numerology - Mobile Number Analysis

A premium Streamlit application for analyzing mobile numbers using ancient numerology principles.

## Features

- **Personal Information**: Input name, date of birth, and mobile number
- **Core Numbers**: Calculate Moolank (birth day) and Bhagyank (destiny number)
- **Number Classification**: Friendly, enemy, and neutral numbers based on Moolank
- **Pair Analysis**: Analyze mobile number digit pairs with color-coded results
- **Final Result**: Overall mobile number compatibility assessment
- **Remedies & Recommendations**: 
  - Charging directions
  - Lucky colors
  - Recommended crystals with purchase link

## Special Features

- **Exceptional Rule**: Bidirectional enemy relationship between numbers 3 and 6
- **Crystal Recommendations**: Based on missing numbers from Lo Shu Grid (backend only)
- **Modern Spiritual Design**: Golden theme with Cinzel fonts
- **Responsive Layout**: Works on all devices

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## Project Structure

```
mobile numerology/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
└── mobile_numerology/        # Core numerology logic
    ├── __init__.py
    └── consultation.py       # Numerology calculations
```

## Deployment

This application is ready for deployment on:
- Streamlit Cloud
- Heroku
- AWS
- Any platform supporting Python web applications

## Numerology Logic

The application uses traditional numerology principles:
- **Moolank**: Sum of birth day digits
- **Bhagyank**: Sum of all date of birth digits
- **Lo Shu Grid**: Ancient 3x3 grid for number placement
- **Compatibility**: Predefined relationships between numbers
- **Exceptional Rule**: Numbers 3 and 6 are mutual enemies

## Contact

For support or inquiries, please refer to the crystal recommendation link in the app.
