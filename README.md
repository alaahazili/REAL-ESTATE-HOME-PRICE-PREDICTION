# 🏠 House Price Prediction System

A machine learning-based web application for predicting property prices in Morocco using scraped real estate data. The system uses a Linear Regression model to estimate property values based on various features like location, property type, number of bedrooms/bathrooms, and area.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Model Details](#model-details)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## ✨ Features

- **Web-based Interface**: User-friendly Flask web application
- **Real-time Predictions**: Instant property price predictions
- **Multiple Property Types**: Support for Villas, Apartments, and other property types
- **Location-based Pricing**: Considers different neighborhoods (Souissi, Hay Riad, etc.)
- **Responsive Design**: Mobile-friendly interface with modern styling
- **Data Scraping**: Automated data collection from real estate websites
- **Machine Learning Model**: Trained Linear Regression model for accurate predictions

## 📁 Project Structure

```
HousePrediction/
├── app/                          # Flask web application
│   ├── templates/
│   │   └── index.html           # Main web interface
│   ├── statics/
│   │   └── style.css            # CSS styling
│   ├── app.py                   # Flask application logic
│   ├── linear_regression_model.pkl  # Trained ML model
│   ├── feature_columns.pkl      # Feature column definitions
│   └── house.webp               # Background image
├── modelTrainnig/               # Model training notebooks
│   ├── input/
│   │   └── properties.csv       # Training dataset
│   └── main.ipynb               # Jupyter notebook for model training
├── Scrapping/                   # Data scraping scripts
│   ├── output/
│   │   └── properties.csv       # Scraped data output
│   └── ScrappingData.ipynb      # Data scraping notebook
└── properties.csv               # Main dataset
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone <https://github.com/alaahazili/REAL-ESTATE-HOME-PRICE-PREDICTION.git>
cd HousePrediction
```

### Step 2: Install Dependencies

Create a virtual environment (recommended):

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

Install required packages:

```bash
pip install flask pandas scikit-learn joblib numpy
```

Or create a `requirements.txt` file:

```txt
Flask==2.3.3
pandas==2.0.3
scikit-learn==1.3.0
joblib==1.3.2
numpy==1.24.3
```

Then install:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
cd app
python app.py
```

The application will be available at `http://localhost:5000`

## 💻 Usage

### Web Interface

1. **Open your browser** and navigate to `http://localhost:5000`
2. **Fill in the property details**:
   - Number of bedrooms
   - Number of bathrooms
   - Area (in square meters)
   - Location (Souissi or Other)
   - Property type (Villa or Other)
3. **Click "Predict"** to get the estimated property price
4. **View the result** displayed in Moroccan Dirhams (MAD)

### Example Input

```
Bedrooms: 3
Bathrooms: 2
Area: 150
Location: Souissi
Property Type: Villa
```

**Expected Output**: `Predicted Price: 1,500,000.00 MAD`

## 📊 Data Sources

The project uses real estate data scraped from Moroccan property websites, including:

- **Property Types**: Villas, Apartments, Duplex, Triplex, Riad, Terrain
- **Locations**: Souissi, Hay Riad, Agdal, Hassan, El Menzeh, and others
- **Features**: Price, bedrooms, bathrooms, area, location, property type
- **Dataset Size**: 252 properties with complete information

## 🤖 Model Details

### Machine Learning Approach

- **Algorithm**: Linear Regression
- **Features Used**:
  - Number of bedrooms
  - Number of bathrooms
  - Scaled area
  - Location (one-hot encoded)
  - Property type (one-hot encoded)

### Model Performance

The model is trained on real estate data from Morocco and provides:
- Price predictions in Moroccan Dirhams (KMAD)
- Location-specific pricing adjustments
- Property type-based valuations

### Feature Engineering

- **Area Scaling**: Area values are normalized for better model performance
- **Categorical Encoding**: Location and property type are one-hot encoded
- **Feature Selection**: Only relevant features are used for prediction

## 🛠️ Technologies Used

### Backend
- **Flask**: Web framework for the application
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning library
- **Joblib**: Model serialization

### Frontend
- **HTML5**: Web page structure
- **CSS3**: Styling and responsive design
- **JavaScript**: Form handling and user interactions

### Data Processing
- **Jupyter Notebooks**: Data analysis and model training
- **Web Scraping**: Automated data collection

## 🔧 Development

### Training New Models

1. Navigate to `modelTrainnig/` directory
2. Open `main.ipynb` in Jupyter Notebook
3. Modify the training parameters as needed
4. Run the notebook to generate new model files
5. Replace the existing `.pkl` files in the `app/` directory

### Data Scraping

1. Navigate to `Scrapping/` directory
2. Open `ScrappingData.ipynb` in Jupyter Notebook
3. Run the scraping scripts to collect new data
4. Update the dataset files as needed

