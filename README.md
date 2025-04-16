# 🎓 Perceived Parental Pressure Predictor

This project analyzes the psychological impact of parental expectations on students through data analytics and machine learning. It features a Streamlit-based web app to predict the **perceived level of parental pressure** based on responses to 15 well-structured questions.

---

## 📊 Problem Statement

Students often face immense academic and career pressure from their parents. This project aims to:

- Quantify and categorize perceived parental pressure.
- Analyze the relationship between responses and pressure levels.
- Use an SVM classifier to predict pressure levels in real-time.

---

## 💡 Key Features

- **15-Question Interface**: Covers academic expectations, emotional impact, peer comparisons, and autonomy.
- **Pressure Levels**: 
  - No Pressure
  - Low Pressure
  - Moderate Pressure
  - High Pressure
  - Very High Pressure
- **Interactive Streamlit App**: Simple UI with instant predictions.
- **ML Model**: Trained using SVM with SMOTE for class balance and StandardScaler for feature scaling.

---

## 🛠 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn (SVM, SMOTE)
- Streamlit (Frontend)
- Pickle (Model Serialization)

---



## 🚀 How to Run the App

1. Clone the repo:
    ```
    git clone https://github.com/yourusername/perceived-parental-pressure.git
    cd perceived-parental-pressure
    ```

2. Install required packages:
    ```
    pip install -r requirements.txt
    ```

3. Run the app:
    ```
    streamlit run pressure.py
    ```

4. The app will open in your browser at: [http://localhost:8501](http://localhost:8501)

---

## 🧠 Dataset

- Contains student responses to 15 questions.
- Target column: `pressure` (Categorical – No, Low, Moderate, High, Very High)
- Balanced using SMOTE for effective training.

---

## 📌 Note

- This is an **educational project** and not intended for clinical diagnosis.
- Encourages awareness around mental health and academic pressure.

---

## 👩‍💻 Author

**Anwesha Pal**  
BCA Student – Data Analytics | Jain (Deemed-to-be) University  
[LinkedIn](#https://www.linkedin.com/in/anwesha-pal-6b6738284/) | [Email](#palanwesha974@gmail.com)

---

## ⭐️ Show Some Love

If you liked this project, consider giving it a ⭐️ on GitHub!

