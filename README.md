GENETIC ALGORITHM FEATURE SELECTION PROJECT
===========================================

PROJECT STRUCTURE:
------------------

genetic-feature-selection/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore file
│
├── genetic_algorithm/              # Student 2 responsibility
│   ├── __init__.py
│   ├── chromosome.py               # Chromosome representation
│   ├── fitness.py                  # Fitness evaluation functions
│   ├── operators.py                # Selection, Crossover, Mutation
│   └── ga_engine.py                # Main GA execution engine
│
├── data_processing/                # Student 1 responsibility
│   ├── __init__.py
│   ├── loader.py                   # Data loading utilities
│   ├── preprocessor.py             # Data preprocessing
│   └── validator.py                # Data validation
│
├── models/                         # Student 3 responsibility
│   ├── __init__.py
│   ├── ml_models.py                # ML model implementations
│   ├── evaluator.py                # Model evaluation
│   └── metrics.py                  # Performance metrics
│
├── comparison/                     # Student 6 responsibility
│   ├── __init__.py
│   ├── traditional_methods.py      # Traditional feature selection
│   └── statistical_analysis.py     # Statistical comparisons
│
├── web/                            # Student 4 & 5 responsibility
│   ├── __init__.py
│   ├── routes.py                   # Flask routes (Student 5)
│   ├── templates/                  # HTML templates (Student 4)
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── upload.html
│   │   ├── results.html
│   │   └── comparison.html
│   └── static/                     # CSS, JS, Images (Student 4)
│       ├── css/
│       ├── js/
│       └── img/
│
├── sample_datasets/                # Testing datasets
│   ├── iris.csv
│   ├── breast_cancer.csv
│   ├── wine_quality.csv
│   └── sonar.csv
│
├── tests/                          # Unit tests
│   ├── __init__.py
│   ├── test_ga.py
│   ├── test_data.py
│   └── test_models.py
│
└── results/                        # Output results
    └── experiments/

WORKFLOW:
---------

1. User uploads CSV file → data_processing (Student 1)
2. Data validated & preprocessed → genetic_algorithm (Student 2)
3. GA runs feature selection → models (Student 3)
4. Models trained & evaluated → comparison (Student 6)
5. Results compared with traditional methods → web (Student 4, 5)
6. Results displayed beautifully on web interface

GIT WORKFLOW:
-------------

main branch
├── develop branch
│   ├── feature/data-processing (Student 1)
│   ├── feature/genetic-algorithm (Student 2)
│   ├── feature/ml-models (Student 3)
│   ├── feature/frontend (Student 4)
│   ├── feature/backend (Student 5)
│   └── feature/comparison (Student 6)

TIMELINE (10 weeks):
--------------------

Week 1-2: Setup & Data Processing (Student 1)
Week 2-4: GA Core Implementation (Student 2)
Week 3-5: ML Models & Evaluation (Student 3)
Week 4-6: Frontend Development (Student 4)
Week 5-7: Backend Integration (Student 5)
Week 6-8: Comparison & Analysis (Student 6)
Week 8-9: Testing & Integration
Week 10: Deployment & Final Documentation

GRADING CHECKLIST:
------------------

[ ] الكود (30 points)
    - Clean, well-structured code
    - Comments in English
    - Follows Python best practices
    
[ ] تطبيق الخوارزمية الجينية (30 points)
    - Correct implementation
    - Proper chromosome representation
    - Effective fitness function
    - Working GA operators
    
[ ] GitHub (10 points)
    - Regular commits from all students
    - Clear commit messages
    - Branch strategy
    - Pull requests & code reviews
    
[ ] واجهات الويب (10 points)
    - Modern, clean UI
    - Responsive design
    - Good UX
    - Interactive visualizations
    
[ ] التقرير (10 points)
    - Complete documentation
    - Results analysis
    - Methodology explanation
    
[ ] الاستضافة (10 points)
    - Working deployed version
    - Accessible online
    - Stable performance

