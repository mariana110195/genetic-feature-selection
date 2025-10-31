═══════════════════════════════════════════════════════════════════════════════
خطة مشروع اختيار الميزات باستخدام الخوارزميات الجينية
Genetic Algorithm Feature Selection Project Plan
═══════════════════════════════════════════════════════════════════════════════

📋 نظرة عامة على المشروع
════════════════════════════

الهدف: تطوير نظام ذكي لاختيار الميزات الأكثر أهمية من مجموعات البيانات الضخمة
       باستخدام الخوارزميات الجينية (Genetic Algorithms)

التقنيات المستخدمة:
- اللغة: Python 3.8+
- الواجهة: Flask Web Application
- المكتبات: NumPy, Pandas, Scikit-learn, Matplotlib, Plotly
- التحكم بالإصدارات: Git & GitHub

════════════════════════════════════════════════════════════════════════════════
👥 توزيع الأدوار على 6 طلاب
════════════════════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 1: Data Processing Engineer (مهندس معالجة البيانات)                │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات:                                                                 │
│   ✓ تحميل البيانات من ملفات CSV وExcel                                     │
│   ✓ التحقق من صحة البيانات (Data Validation)                               │
│   ✓ المعالجة المسبقة (Preprocessing)                                        │
│     - تنظيف البيانات                                                        │
│     - معالجة القيم المفقودة                                                 │
│     - تحويل البيانات الفئوية إلى رقمية (Encoding)                           │
│     - التطبيع (Normalization/Standardization)                               │
│   ✓ تقسيم البيانات (Train/Test Split)                                      │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - data_processing/loader.py                                                │
│   - data_processing/preprocessor.py                                          │
│   - data_processing/validator.py                                             │
│                                                                              │
│ Branch: feature/data-processing                                              │
│ الوقت المقدر: أسبوعان (Week 1-2)                                            │
│ النسبة من المشروع: 15%                                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 2: Genetic Algorithm Core Developer (مطور نواة الخوارزمية الجينية) │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات: (هذا هو الجزء الأهم من المشروع!)                               │
│   ✓ تصميم تمثيل الكروموسوم (Chromosome Representation)                      │
│     - Binary encoding للميزات (1 = selected, 0 = not selected)             │
│   ✓ تطوير دالة اللياقة (Fitness Function)                                  │
│     - تدريب نموذج ML على الميزات المختارة                                   │
│     - حساب دقة النموذج                                                       │
│     - الموازنة بين الدقة وعدد الميزات                                       │
│   ✓ تنفيذ عمليات GA الأساسية:                                              │
│     - Selection (Tournament, Roulette Wheel)                                 │
│     - Crossover (Single-point, Two-point, Uniform)                           │
│     - Mutation (Bit-flip)                                                    │
│     - Elitism (حفظ أفضل الأفراد)                                            │
│   ✓ محرك تشغيل GA الرئيسي                                                   │
│     - إنشاء Population الأولي                                               │
│     - حلقة التطور (Evolution Loop)                                           │
│     - معايير التوقف (Stopping Criteria)                                     │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - genetic_algorithm/chromosome.py                                          │
│   - genetic_algorithm/fitness.py                                             │
│   - genetic_algorithm/operators.py                                           │
│   - genetic_algorithm/ga_engine.py                                           │
│                                                                              │
│ Branch: feature/genetic-algorithm                                            │
│ الوقت المقدر: 3 أسابيع (Week 2-4)                                           │
│ النسبة من المشروع: 25% ⭐ الأهم                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 3: ML Models & Evaluation Specialist (متخصص نماذج التعلم الآلي)     │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات:                                                                 │
│   ✓ تنفيذ نماذج ML متعددة:                                                  │
│     - Random Forest                                                          │
│     - Support Vector Machine (SVM)                                           │
│     - K-Nearest Neighbors (KNN)                                              │
│     - Decision Tree                                                          │
│   ✓ نظام تقييم شامل:                                                        │
│     - Accuracy, Precision, Recall, F1-Score                                  │
│     - Confusion Matrix                                                       │
│     - Cross-validation                                                       │
│     - ROC-AUC Curve                                                          │
│   ✓ مقارنة الأداء:                                                          │
│     - قبل اختيار الميزات (All features)                                     │
│     - بعد اختيار الميزات (GA selected)                                      │
│   ✓ تتبع أداء GA عبر الأجيال                                                │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - models/ml_models.py                                                      │
│   - models/evaluator.py                                                      │
│   - models/metrics.py                                                        │
│                                                                              │
│ Branch: feature/ml-models                                                    │
│ الوقت المقدر: 3 أسابيع (Week 3-5)                                           │
│ النسبة من المشروع: 20%                                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 4: Frontend & UI Developer (مطور الواجهة الأمامية)                  │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات:                                                                 │
│   ✓ تصميم واجهات HTML جميلة وعصرية:                                        │
│     - الصفحة الرئيسية (Home)                                                │
│     - صفحة رفع البيانات (Upload)                                            │
│     - صفحة النتائج (Results)                                                │
│     - صفحة المقارنة (Comparison)                                            │
│   ✓ تطوير CSS مخصص:                                                         │
│     - تصميم متجاوب (Responsive Design)                                      │
│     - ألوان وثيمات جذابة                                                    │
│     - رسوم متحركة (Animations)                                              │
│   ✓ JavaScript للتفاعل:                                                     │
│     - رفع الملفات بالسحب والإفلات (Drag & Drop)                             │
│     - تحديث ديناميكي للنتائج                                                │
│     - رسوم بيانية تفاعلية (Charts.js/Plotly)                               │
│   ✓ تحسين تجربة المستخدم (UX)                                               │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - web/templates/*.html                                                     │
│   - web/static/css/                                                          │
│   - web/static/js/                                                           │
│                                                                              │
│ Branch: feature/frontend                                                     │
│ الوقت المقدر: 3 أسابيع (Week 4-6)                                           │
│ النسبة من المشروع: 15%                                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 5: Backend & Integration Engineer (مهندس الخادم والتكامل)           │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات:                                                                 │
│   ✓ تطوير Flask Routes & APIs:                                              │
│     - GET /           → Home page                                            │
│     - GET /upload     → Upload page                                          │
│     - POST /api/upload → File upload handling                                │
│     - POST /api/run-ga → Execute GA                                          │
│     - GET /results    → Results page                                         │
│     - GET /comparison → Comparison page                                      │
│     - POST /api/comparison → Run comparison                                  │
│   ✓ دمج جميع المكونات:                                                      │
│     - ربط Data Processing مع GA                                             │
│     - ربط GA مع ML Models                                                    │
│     - ربط Frontend مع Backend                                               │
│   ✓ معالجة الأخطاء (Error Handling)                                         │
│   ✓ التخزين المؤقت (Caching) لتحسين الأداء                                  │
│   ✓ إدارة الجلسات (Session Management)                                      │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - web/routes.py                                                            │
│   - web/__init__.py                                                          │
│   - app.py                                                                   │
│                                                                              │
│ Branch: feature/backend                                                      │
│ الوقت المقدر: 3 أسابيع (Week 5-7)                                           │
│ النسبة من المشروع: 15%                                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 6: Comparison & Documentation Lead (قائد المقارنة والتوثيق)         │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات:                                                                 │
│   ✓ تنفيذ الطرق التقليدية لاختيار الميزات:                                 │
│     - Chi-Square Test                                                        │
│     - Mutual Information                                                     │
│     - Random Forest Feature Importance                                       │
│     - Correlation-based Feature Selection                                    │
│   ✓ المقارنة الإحصائية:                                                     │
│     - T-test للفروقات                                                       │
│     - ANOVA analysis                                                         │
│     - Wilcoxon signed-rank test                                              │
│   ✓ توليد التقارير:                                                         │
│     - جداول المقارنة                                                        │
│     - رسوم بيانية مقارنة                                                    │
│     - التحليل الإحصائي                                                      │
│   ✓ التوثيق الشامل:                                                         │
│     - Git commits منظمة                                                     │
│     - كتابة README                                                           │
│     - توثيق الكود                                                            │
│   ✓ الاستضافة على الويب (Deployment):                                       │
│     - Heroku / Railway / Render                                              │
│     - إعداد ملفات الاستضافة                                                 │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - comparison/traditional_methods.py                                        │
│   - comparison/statistical_analysis.py                                       │
│   - README.md (عند الطلب)                                                   │
│   - Deployment files                                                         │
│                                                                              │
│ Branch: feature/comparison                                                   │
│ الوقت المقدر: 3 أسابيع (Week 6-8)                                           │
│ النسبة من المشروع: 10%                                                      │
└──────────────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
📊 مجموعات البيانات المتوفرة للاختبار
════════════════════════════════════════════════════════════════════════════════

جميع مجموعات البيانات موجودة في: sample_datasets/

1️⃣ iris.csv (سهل جداً - للبداية)
   ├── الميزات: 4 features
   ├── العينات: 150 samples
   ├── الفئات: 3 classes (Setosa, Versicolor, Virginica)
   └── الاستخدام: الاختبار الأولي والتحقق من صحة الكود

2️⃣ breast_cancer.csv (متوسط - للعرض)
   ├── الميزات: 30 features ← يمكن تقليصها بشكل كبير
   ├── العينات: 569 samples
   ├── الفئات: 2 classes (Malignant, Benign)
   └── الاستخدام: إظهار قدرة GA على تقليل الميزات من 30 إلى ~8

3️⃣ wine.csv (متوسط - للاختبار العام)
   ├── الميزات: 13 features
   ├── العينات: 178 samples
   ├── الفئات: 3 classes
   └── الاستخدام: اختبار متوازن للأداء العام

4️⃣ synthetic_high_dim.csv (صعب - للتحدي)
   ├── الميزات: 50 features (15 فقط مفيدة!)
   ├── العينات: 1000 samples
   ├── الفئات: 2 classes
   └── الاستخدام: إثبات قوة GA في إيجاد الميزات المفيدة بين الميزات الزائفة

5️⃣ synthetic_multiclass.csv (متوسط - متعدد الفئات)
   ├── الميزات: 20 features
   ├── العينات: 800 samples
   ├── الفئات: 4 classes
   └── الاستخدام: اختبار الأداء مع فئات متعددة

6️⃣ small_test.csv (سهل جداً - للتطوير السريع)
   ├── الميزات: 5 features
   ├── العينات: 100 samples
   ├── الفئات: 2 classes
   └── الاستخدام: اختبار سريع أثناء التطوير (تنفيذ في ثوانٍ)

💡 نصيحة: ابدأ دائماً بـ small_test.csv أو iris.csv للتحقق من صحة الكود،
          ثم انتقل إلى breast_cancer.csv أو synthetic_high_dim.csv للعرض

════════════════════════════════════════════════════════════════════════════════
📅 الجدول الزمني (10 أسابيع)
════════════════════════════════════════════════════════════════════════════════

Week 1-2:  [████████████████████████] Setup + Data Processing (Student 1)
Week 2-4:  [████████████████████████] GA Core Implementation (Student 2) ⭐
Week 3-5:  [████████████████████████] ML Models & Evaluation (Student 3)
Week 4-6:  [████████████████████████] Frontend Development (Student 4)
Week 5-7:  [████████████████████████] Backend Integration (Student 5)
Week 6-8:  [████████████████████████] Comparison & Analysis (Student 6)
Week 8-9:  [████████████████████████] Testing & Integration (All Students)
Week 10:   [████████████████████████] Deployment & Documentation (Student 6)

════════════════════════════════════════════════════════════════════════════════
🔄 استراتيجية Git Workflow
════════════════════════════════════════════════════════════════════════════════

main (الفرع الرئيسي - مستقر دائماً)
 │
 └─── develop (فرع التطوير - للدمج المستمر)
       │
       ├─── feature/data-processing     (Student 1)
       ├─── feature/genetic-algorithm   (Student 2)
       ├─── feature/ml-models           (Student 3)
       ├─── feature/frontend            (Student 4)
       ├─── feature/backend             (Student 5)
       └─── feature/comparison          (Student 6)

قواعد Git:
✓ كل طالب يعمل على فرعه الخاص
✓ Commit messages واضحة ومفصلة بالإنجليزية
✓ Pull Request قبل الدمج في develop
✓ Code review من طالب آخر على الأقل
✓ لا تدمج في main إلا بعد اختبار شامل

مثال على Commit Message الجيد:
"feat(ga): implement tournament selection operator
- Add tournament selection with configurable size
- Include unit tests for edge cases
- Update documentation with usage examples"

════════════════════════════════════════════════════════════════════════════════
📝 سلم التصحيح (100 نقطة)
════════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────┐
│ المعيار                           النقاط    الوصف               │
├─────────────────────────────────────────────────────────────────┤
│ 1. الكود (Code Quality)            30      - نظافة الكود        │
│                                             - التنظيم           │
│                                             - التعليقات         │
│                                             - Best practices     │
├─────────────────────────────────────────────────────────────────┤
│ 2. تطبيق GA                        30      - التطبيق الصحيح    │
│                                             - Chromosome design  │
│                                             - Fitness function   │
│                                             - GA operators       │
│                                             - تحسين مستمر       │
├─────────────────────────────────────────────────────────────────┤
│ 3. GitHub                           10      - Commits منتظمة    │
│                                             - Branch strategy    │
│                                             - Pull requests      │
│                                             - Documentation      │
├─────────────────────────────────────────────────────────────────┤
│ 4. واجهات الويب                    10      - تصميم جذاب        │
│                                             - UX ممتاز          │
│                                             - Responsive         │
│                                             - Visualizations     │
├─────────────────────────────────────────────────────────────────┤
│ 5. التقرير                         10      - شامل ومفصل        │
│                                             - منهجية واضحة      │
│                                             - نتائج محللة        │
│                                             - مراجع            │
├─────────────────────────────────────────────────────────────────┤
│ 6. الاستضافة                       10      - يعمل أونلاين      │
│                                             - مستقر             │
│                                             - يمكن الوصول إليه  │
├─────────────────────────────────────────────────────────────────┤
│ المجموع                            100                         │
└─────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
✅ قائمة المهام (Checklist)
════════════════════════════════════════════════════════════════════════════════

Setup & Environment:
  [✓] Create project structure
  [✓] Setup requirements.txt
  [✓] Configure .gitignore
  [✓] Generate sample datasets
  [✓] Initialize Git repository
  [ ] Create GitHub repository
  [ ] Setup CI/CD pipeline

Student 1 - Data Processing:
  [ ] Implement DataLoader class
  [ ] Implement DataPreprocessor class
  [ ] Implement DataValidator class
  [ ] Handle missing values
  [ ] Encode categorical features
  [ ] Normalize/standardize data
  [ ] Write unit tests
  [ ] Documentation

Student 2 - Genetic Algorithm: ⭐
  [ ] Design Chromosome class
  [ ] Implement Fitness Function
  [ ] Implement Selection operators
  [ ] Implement Crossover operators
  [ ] Implement Mutation operators
  [ ] Implement Elitism
  [ ] Create GA Engine
  [ ] Add convergence tracking
  [ ] Write unit tests
  [ ] Documentation

Student 3 - ML Models:
  [ ] Implement Random Forest
  [ ] Implement SVM
  [ ] Implement KNN
  [ ] Create ModelEvaluator class
  [ ] Calculate performance metrics
  [ ] Implement cross-validation
  [ ] Generate confusion matrices
  [ ] Write unit tests
  [ ] Documentation

Student 4 - Frontend:
  [ ] Design base template
  [ ] Create home page
  [ ] Create upload page
  [ ] Create results page
  [ ] Create comparison page
  [ ] Add drag-and-drop upload
  [ ] Implement charts/visualizations
  [ ] Make responsive design
  [ ] Add animations
  [ ] Test on multiple browsers

Student 5 - Backend:
  [ ] Implement Flask routes
  [ ] File upload handling
  [ ] Integrate data processing
  [ ] Integrate GA execution
  [ ] Integrate ML models
  [ ] Error handling
  [ ] Session management
  [ ] API documentation
  [ ] Testing

Student 6 - Comparison & Deployment:
  [ ] Implement Chi-Square
  [ ] Implement Mutual Information
  [ ] Implement RF importance
  [ ] Statistical analysis
  [ ] Generate comparison reports
  [ ] Write README.md
  [ ] Prepare deployment files
  [ ] Deploy to cloud platform
  [ ] Final testing

════════════════════════════════════════════════════════════════════════════════
🚀 البدء السريع (Quick Start)
════════════════════════════════════════════════════════════════════════════════

1. تثبيت المتطلبات:
   pip install -r requirements.txt

2. توليد بيانات الاختبار:
   python generate_sample_data.py

3. تشغيل التطبيق:
   python app.py

4. فتح المتصفح:
   http://localhost:5000

════════════════════════════════════════════════════════════════════════════════
📚 مصادر مفيدة
════════════════════════════════════════════════════════════════════════════════

Genetic Algorithms:
- "Introduction to Genetic Algorithms" - Holland, J.H.
- https://towardsdatascience.com/genetic-algorithm-explained

Feature Selection:
- Scikit-learn Feature Selection Guide
- "Feature Engineering and Selection" - Kuhn & Johnson

Flask:
- Flask Official Documentation: https://flask.palletsprojects.com
- Flask Mega-Tutorial

Machine Learning:
- Scikit-learn Documentation
- "Hands-On Machine Learning" - Aurélien Géron

════════════════════════════════════════════════════════════════════════════════
📞 التواصل والتنسيق
════════════════════════════════════════════════════════════════════════════════

يُنصح بـ:
✓ اجتماع أسبوعي لجميع أعضاء الفريق
✓ استخدام GitHub Issues لتتبع المشاكل
✓ استخدام Pull Requests للمراجعة
✓ توثيق كل شيء في Git

════════════════════════════════════════════════════════════════════════════════

تم إعداد هذه الخطة بواسطة: AI Assistant
التاريخ: 31 أكتوبر 2025

حظاً موفقاً لجميع الطلاب! 🎓

═══════════════════════════════════════════════════════════════════════════════
خطة مشروع اختيار الميزات باستخدام الخوارزميات الجينية
Genetic Algorithm Feature Selection Project Plan
═══════════════════════════════════════════════════════════════════════════════

📋 نظرة عامة على المشروع
════════════════════════════

الهدف: تطوير نظام ذكي لاختيار الميزات الأكثر أهمية من مجموعات البيانات الضخمة
       باستخدام الخوارزميات الجينية (Genetic Algorithms)

التقنيات المستخدمة:
- اللغة: Python 3.8+
- الواجهة: Flask Web Application
- المكتبات: NumPy, Pandas, Scikit-learn, Matplotlib, Plotly
- التحكم بالإصدارات: Git & GitHub

════════════════════════════════════════════════════════════════════════════════
👥 توزيع الأدوار على 6 طلاب
════════════════════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 1: Data Processing Engineer (مهندس معالجة البيانات)                │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات:                                                                 │
│   ✓ تحميل البيانات من ملفات CSV وExcel                                     │
│   ✓ التحقق من صحة البيانات (Data Validation)                               │
│   ✓ المعالجة المسبقة (Preprocessing)                                        │
│     - تنظيف البيانات                                                        │
│     - معالجة القيم المفقودة                                                 │
│     - تحويل البيانات الفئوية إلى رقمية (Encoding)                           │
│     - التطبيع (Normalization/Standardization)                               │
│   ✓ تقسيم البيانات (Train/Test Split)                                      │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - data_processing/loader.py                                                │
│   - data_processing/preprocessor.py                                          │
│   - data_processing/validator.py                                             │
│                                                                              │
│ Branch: feature/data-processing                                              │
│ الوقت المقدر: أسبوعان (Week 1-2)                                            │
│ النسبة من المشروع: 15%                                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 2: Genetic Algorithm Core Developer (مطور نواة الخوارزمية الجينية) │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات: (هذا هو الجزء الأهم من المشروع!)                               │
│   ✓ تصميم تمثيل الكروموسوم (Chromosome Representation)                      │
│     - Binary encoding للميزات (1 = selected, 0 = not selected)             │
│   ✓ تطوير دالة اللياقة (Fitness Function)                                  │
│     - تدريب نموذج ML على الميزات المختارة                                   │
│     - حساب دقة النموذج                                                       │
│     - الموازنة بين الدقة وعدد الميزات                                       │
│   ✓ تنفيذ عمليات GA الأساسية:                                              │
│     - Selection (Tournament, Roulette Wheel)                                 │
│     - Crossover (Single-point, Two-point, Uniform)                           │
│     - Mutation (Bit-flip)                                                    │
│     - Elitism (حفظ أفضل الأفراد)                                            │
│   ✓ محرك تشغيل GA الرئيسي                                                   │
│     - إنشاء Population الأولي                                               │
│     - حلقة التطور (Evolution Loop)                                           │
│     - معايير التوقف (Stopping Criteria)                                     │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - genetic_algorithm/chromosome.py                                          │
│   - genetic_algorithm/fitness.py                                             │
│   - genetic_algorithm/operators.py                                           │
│   - genetic_algorithm/ga_engine.py                                           │
│                                                                              │
│ Branch: feature/genetic-algorithm                                            │
│ الوقت المقدر: 3 أسابيع (Week 2-4)                                           │
│ النسبة من المشروع: 25% ⭐ الأهم                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 3: ML Models & Evaluation Specialist (متخصص نماذج التعلم الآلي)     │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات:                                                                 │
│   ✓ تنفيذ نماذج ML متعددة:                                                  │
│     - Random Forest                                                          │
│     - Support Vector Machine (SVM)                                           │
│     - K-Nearest Neighbors (KNN)                                              │
│     - Decision Tree                                                          │
│   ✓ نظام تقييم شامل:                                                        │
│     - Accuracy, Precision, Recall, F1-Score                                  │
│     - Confusion Matrix                                                       │
│     - Cross-validation                                                       │
│     - ROC-AUC Curve                                                          │
│   ✓ مقارنة الأداء:                                                          │
│     - قبل اختيار الميزات (All features)                                     │
│     - بعد اختيار الميزات (GA selected)                                      │
│   ✓ تتبع أداء GA عبر الأجيال                                                │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - models/ml_models.py                                                      │
│   - models/evaluator.py                                                      │
│   - models/metrics.py                                                        │
│                                                                              │
│ Branch: feature/ml-models                                                    │
│ الوقت المقدر: 3 أسابيع (Week 3-5)                                           │
│ النسبة من المشروع: 20%                                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 4: Frontend & UI Developer (مطور الواجهة الأمامية)                  │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات:                                                                 │
│   ✓ تصميم واجهات HTML جميلة وعصرية:                                        │
│     - الصفحة الرئيسية (Home)                                                │
│     - صفحة رفع البيانات (Upload)                                            │
│     - صفحة النتائج (Results)                                                │
│     - صفحة المقارنة (Comparison)                                            │
│   ✓ تطوير CSS مخصص:                                                         │
│     - تصميم متجاوب (Responsive Design)                                      │
│     - ألوان وثيمات جذابة                                                    │
│     - رسوم متحركة (Animations)                                              │
│   ✓ JavaScript للتفاعل:                                                     │
│     - رفع الملفات بالسحب والإفلات (Drag & Drop)                             │
│     - تحديث ديناميكي للنتائج                                                │
│     - رسوم بيانية تفاعلية (Charts.js/Plotly)                               │
│   ✓ تحسين تجربة المستخدم (UX)                                               │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - web/templates/*.html                                                     │
│   - web/static/css/                                                          │
│   - web/static/js/                                                           │
│                                                                              │
│ Branch: feature/frontend                                                     │
│ الوقت المقدر: 3 أسابيع (Week 4-6)                                           │
│ النسبة من المشروع: 15%                                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 5: Backend & Integration Engineer (مهندس الخادم والتكامل)           │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات:                                                                 │
│   ✓ تطوير Flask Routes & APIs:                                              │
│     - GET /           → Home page                                            │
│     - GET /upload     → Upload page                                          │
│     - POST /api/upload → File upload handling                                │
│     - POST /api/run-ga → Execute GA                                          │
│     - GET /results    → Results page                                         │
│     - GET /comparison → Comparison page                                      │
│     - POST /api/comparison → Run comparison                                  │
│   ✓ دمج جميع المكونات:                                                      │
│     - ربط Data Processing مع GA                                             │
│     - ربط GA مع ML Models                                                    │
│     - ربط Frontend مع Backend                                               │
│   ✓ معالجة الأخطاء (Error Handling)                                         │
│   ✓ التخزين المؤقت (Caching) لتحسين الأداء                                  │
│   ✓ إدارة الجلسات (Session Management)                                      │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - web/routes.py                                                            │
│   - web/__init__.py                                                          │
│   - app.py                                                                   │
│                                                                              │
│ Branch: feature/backend                                                      │
│ الوقت المقدر: 3 أسابيع (Week 5-7)                                           │
│ النسبة من المشروع: 15%                                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ الطالب 6: Comparison & Documentation Lead (قائد المقارنة والتوثيق)         │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ المسؤوليات:                                                                 │
│   ✓ تنفيذ الطرق التقليدية لاختيار الميزات:                                 │
│     - Chi-Square Test                                                        │
│     - Mutual Information                                                     │
│     - Random Forest Feature Importance                                       │
│     - Correlation-based Feature Selection                                    │
│   ✓ المقارنة الإحصائية:                                                     │
│     - T-test للفروقات                                                       │
│     - ANOVA analysis                                                         │
│     - Wilcoxon signed-rank test                                              │
│   ✓ توليد التقارير:                                                         │
│     - جداول المقارنة                                                        │
│     - رسوم بيانية مقارنة                                                    │
│     - التحليل الإحصائي                                                      │
│   ✓ التوثيق الشامل:                                                         │
│     - Git commits منظمة                                                     │
│     - كتابة README                                                           │
│     - توثيق الكود                                                            │
│   ✓ الاستضافة على الويب (Deployment):                                       │
│     - Heroku / Railway / Render                                              │
│     - إعداد ملفات الاستضافة                                                 │
│                                                                              │
│ الملفات المسؤول عنها:                                                       │
│   - comparison/traditional_methods.py                                        │
│   - comparison/statistical_analysis.py                                       │
│   - README.md (عند الطلب)                                                   │
│   - Deployment files                                                         │
│                                                                              │
│ Branch: feature/comparison                                                   │
│ الوقت المقدر: 3 أسابيع (Week 6-8)                                           │
│ النسبة من المشروع: 10%                                                      │
└──────────────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
📊 مجموعات البيانات المتوفرة للاختبار
════════════════════════════════════════════════════════════════════════════════

جميع مجموعات البيانات موجودة في: sample_datasets/

1️⃣ iris.csv (سهل جداً - للبداية)
   ├── الميزات: 4 features
   ├── العينات: 150 samples
   ├── الفئات: 3 classes (Setosa, Versicolor, Virginica)
   └── الاستخدام: الاختبار الأولي والتحقق من صحة الكود

2️⃣ breast_cancer.csv (متوسط - للعرض)
   ├── الميزات: 30 features ← يمكن تقليصها بشكل كبير
   ├── العينات: 569 samples
   ├── الفئات: 2 classes (Malignant, Benign)
   └── الاستخدام: إظهار قدرة GA على تقليل الميزات من 30 إلى ~8

3️⃣ wine.csv (متوسط - للاختبار العام)
   ├── الميزات: 13 features
   ├── العينات: 178 samples
   ├── الفئات: 3 classes
   └── الاستخدام: اختبار متوازن للأداء العام

4️⃣ synthetic_high_dim.csv (صعب - للتحدي)
   ├── الميزات: 50 features (15 فقط مفيدة!)
   ├── العينات: 1000 samples
   ├── الفئات: 2 classes
   └── الاستخدام: إثبات قوة GA في إيجاد الميزات المفيدة بين الميزات الزائفة

5️⃣ synthetic_multiclass.csv (متوسط - متعدد الفئات)
   ├── الميزات: 20 features
   ├── العينات: 800 samples
   ├── الفئات: 4 classes
   └── الاستخدام: اختبار الأداء مع فئات متعددة

6️⃣ small_test.csv (سهل جداً - للتطوير السريع)
   ├── الميزات: 5 features
   ├── العينات: 100 samples
   ├── الفئات: 2 classes
   └── الاستخدام: اختبار سريع أثناء التطوير (تنفيذ في ثوانٍ)

💡 نصيحة: ابدأ دائماً بـ small_test.csv أو iris.csv للتحقق من صحة الكود،
          ثم انتقل إلى breast_cancer.csv أو synthetic_high_dim.csv للعرض

════════════════════════════════════════════════════════════════════════════════
📅 الجدول الزمني (10 أسابيع)
════════════════════════════════════════════════════════════════════════════════

Week 1-2:  [████████████████████████] Setup + Data Processing (Student 1)
Week 2-4:  [████████████████████████] GA Core Implementation (Student 2) ⭐
Week 3-5:  [████████████████████████] ML Models & Evaluation (Student 3)
Week 4-6:  [████████████████████████] Frontend Development (Student 4)
Week 5-7:  [████████████████████████] Backend Integration (Student 5)
Week 6-8:  [████████████████████████] Comparison & Analysis (Student 6)
Week 8-9:  [████████████████████████] Testing & Integration (All Students)
Week 10:   [████████████████████████] Deployment & Documentation (Student 6)

════════════════════════════════════════════════════════════════════════════════
🔄 استراتيجية Git Workflow
════════════════════════════════════════════════════════════════════════════════

main (الفرع الرئيسي - مستقر دائماً)
 │
 └─── develop (فرع التطوير - للدمج المستمر)
       │
       ├─── feature/data-processing     (Student 1)
       ├─── feature/genetic-algorithm   (Student 2)
       ├─── feature/ml-models           (Student 3)
       ├─── feature/frontend            (Student 4)
       ├─── feature/backend             (Student 5)
       └─── feature/comparison          (Student 6)

قواعد Git:
✓ كل طالب يعمل على فرعه الخاص
✓ Commit messages واضحة ومفصلة بالإنجليزية
✓ Pull Request قبل الدمج في develop
✓ Code review من طالب آخر على الأقل
✓ لا تدمج في main إلا بعد اختبار شامل

مثال على Commit Message الجيد:
"feat(ga): implement tournament selection operator
- Add tournament selection with configurable size
- Include unit tests for edge cases
- Update documentation with usage examples"

════════════════════════════════════════════════════════════════════════════════
📝 سلم التصحيح (100 نقطة)
════════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────┐
│ المعيار                           النقاط    الوصف               │
├─────────────────────────────────────────────────────────────────┤
│ 1. الكود (Code Quality)            30      - نظافة الكود        │
│                                             - التنظيم           │
│                                             - التعليقات         │
│                                             - Best practices     │
├─────────────────────────────────────────────────────────────────┤
│ 2. تطبيق GA                        30      - التطبيق الصحيح    │
│                                             - Chromosome design  │
│                                             - Fitness function   │
│                                             - GA operators       │
│                                             - تحسين مستمر       │
├─────────────────────────────────────────────────────────────────┤
│ 3. GitHub                           10      - Commits منتظمة    │
│                                             - Branch strategy    │
│                                             - Pull requests      │
│                                             - Documentation      │
├─────────────────────────────────────────────────────────────────┤
│ 4. واجهات الويب                    10      - تصميم جذاب        │
│                                             - UX ممتاز          │
│                                             - Responsive         │
│                                             - Visualizations     │
├─────────────────────────────────────────────────────────────────┤
│ 5. التقرير                         10      - شامل ومفصل        │
│                                             - منهجية واضحة      │
│                                             - نتائج محللة        │
│                                             - مراجع            │
├─────────────────────────────────────────────────────────────────┤
│ 6. الاستضافة                       10      - يعمل أونلاين      │
│                                             - مستقر             │
│                                             - يمكن الوصول إليه  │
├─────────────────────────────────────────────────────────────────┤
│ المجموع                            100                         │
└─────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
✅ قائمة المهام (Checklist)
════════════════════════════════════════════════════════════════════════════════

Setup & Environment:
  [✓] Create project structure
  [✓] Setup requirements.txt
  [✓] Configure .gitignore
  [✓] Generate sample datasets
  [✓] Initialize Git repository
  [ ] Create GitHub repository
  [ ] Setup CI/CD pipeline

Student 1 - Data Processing:
  [ ] Implement DataLoader class
  [ ] Implement DataPreprocessor class
  [ ] Implement DataValidator class
  [ ] Handle missing values
  [ ] Encode categorical features
  [ ] Normalize/standardize data
  [ ] Write unit tests
  [ ] Documentation

Student 2 - Genetic Algorithm: ⭐
  [ ] Design Chromosome class
  [ ] Implement Fitness Function
  [ ] Implement Selection operators
  [ ] Implement Crossover operators
  [ ] Implement Mutation operators
  [ ] Implement Elitism
  [ ] Create GA Engine
  [ ] Add convergence tracking
  [ ] Write unit tests
  [ ] Documentation

Student 3 - ML Models:
  [ ] Implement Random Forest
  [ ] Implement SVM
  [ ] Implement KNN
  [ ] Create ModelEvaluator class
  [ ] Calculate performance metrics
  [ ] Implement cross-validation
  [ ] Generate confusion matrices
  [ ] Write unit tests
  [ ] Documentation

Student 4 - Frontend:
  [ ] Design base template
  [ ] Create home page
  [ ] Create upload page
  [ ] Create results page
  [ ] Create comparison page
  [ ] Add drag-and-drop upload
  [ ] Implement charts/visualizations
  [ ] Make responsive design
  [ ] Add animations
  [ ] Test on multiple browsers

Student 5 - Backend:
  [ ] Implement Flask routes
  [ ] File upload handling
  [ ] Integrate data processing
  [ ] Integrate GA execution
  [ ] Integrate ML models
  [ ] Error handling
  [ ] Session management
  [ ] API documentation
  [ ] Testing

Student 6 - Comparison & Deployment:
  [ ] Implement Chi-Square
  [ ] Implement Mutual Information
  [ ] Implement RF importance
  [ ] Statistical analysis
  [ ] Generate comparison reports
  [ ] Write README.md
  [ ] Prepare deployment files
  [ ] Deploy to cloud platform
  [ ] Final testing

════════════════════════════════════════════════════════════════════════════════
🚀 البدء السريع (Quick Start)
════════════════════════════════════════════════════════════════════════════════

1. تثبيت المتطلبات:
   pip install -r requirements.txt

2. توليد بيانات الاختبار:
   python generate_sample_data.py

3. تشغيل التطبيق:
   python app.py

4. فتح المتصفح:
   http://localhost:5000

════════════════════════════════════════════════════════════════════════════════
📚 مصادر مفيدة
════════════════════════════════════════════════════════════════════════════════

Genetic Algorithms:
- "Introduction to Genetic Algorithms" - Holland, J.H.
- https://towardsdatascience.com/genetic-algorithm-explained

Feature Selection:
- Scikit-learn Feature Selection Guide
- "Feature Engineering and Selection" - Kuhn & Johnson

Flask:
- Flask Official Documentation: https://flask.palletsprojects.com
- Flask Mega-Tutorial

Machine Learning:
- Scikit-learn Documentation
- "Hands-On Machine Learning" - Aurélien Géron

════════════════════════════════════════════════════════════════════════════════
📞 التواصل والتنسيق
════════════════════════════════════════════════════════════════════════════════

يُنصح بـ:
✓ اجتماع أسبوعي لجميع أعضاء الفريق
✓ استخدام GitHub Issues لتتبع المشاكل
✓ استخدام Pull Requests للمراجعة
✓ توثيق كل شيء في Git

════════════════════════════════════════════════════════════════════════════════

تم إعداد هذه الخطة بواسطة: AI Assistant
التاريخ: 31 أكتوبر 2025

حظاً موفقاً لجميع الطلاب! 🎓

