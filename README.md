# Genetic Algorithm Feature Selection

A comprehensive web-based system for feature selection using Genetic Algorithms.

## Team Members

- **Student 1**: Data Processing Engineer
- **Student 2**: Genetic Algorithm Core Developer
- **Student 3**: ML Models & Evaluation Specialist
- **Student 4**: Frontend Developer
- **Student 5**: Backend & Integration Engineer
- **Student 6**: Web Integration & Deployment Engineer

## Features

- Upload CSV/Excel datasets
- Automatic data preprocessing
- Genetic Algorithm for optimal feature selection
- Multiple ML models (Random Forest, SVM, KNN)
- Performance evaluation and visualization
- Comparison with traditional feature selection methods
- Interactive web interface

## Installation

```bash
pip install -r requirements.txt
```

## Generate Sample Datasets

```bash
python generate_sample_data.py
```

## Run Application

```bash
python app.py
```

Then open: http://localhost:5000

## Technology Stack

- **Backend**: Python, Flask
- **ML Libraries**: Scikit-learn, NumPy, Pandas
- **Visualization**: Matplotlib, Plotly, Chart.js
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5

## Project Structure

```
genetic-feature-selection/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── genetic_algorithm/          # GA implementation (Student 2)
├── data_processing/            # Data handling (Student 1)
├── models/                     # ML models (Student 3)
├── comparison/                 # Method comparison (Student 6)
├── web/                        # Web interface (Student 4 & 5)
│   ├── templates/              # HTML templates
│   ├── static/                 # CSS, JS, images
│   └── routes.py               # API endpoints
└── sample_datasets/            # Test datasets
```

## Sample Datasets

- `iris.csv` - 4 features, 150 samples
- `breast_cancer.csv` - 30 features, 569 samples
- `wine.csv` - 13 features, 178 samples
- `synthetic_high_dim.csv` - 50 features, 1000 samples
- `synthetic_multiclass.csv` - 20 features, 800 samples
- `small_test.csv` - 5 features, 100 samples

## Usage

1. Navigate to the upload page
2. Upload your dataset or select a sample dataset
3. Configure GA parameters (population size, generations, etc.)
4. Run the genetic algorithm
5. View results and selected features
6. Compare with traditional methods

## Deployment

Deployed on: [PythonAnywhere URL will be here]

## License

Academic Project - 2025

