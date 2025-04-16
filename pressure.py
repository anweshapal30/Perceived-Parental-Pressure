import streamlit as st
import pickle
import numpy as np

# Load the trained SVM model and scaler
with open('/Users/anu/Downloads/svm_model2.pkl', 'rb') as f:
    model = pickle.load(f)

with open('/Users/anu/Downloads/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Function to make prediction
def predict_pressure(inputs):
    scaled_inputs = scaler.transform([inputs])
    prediction = model.predict(scaled_inputs)
    return prediction[0]

# Mapping from prediction value to label
label_map = {
    0: "No Pressure",
    1: "Low Pressure",
    2: "Moderate Pressure",
    3: "High Pressure",
    4: "Very High Pressure"
}

# Options for answers (updated)
options = {
    "No": 0,
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Very High": 4
}

st.title("Parental Pressure Prediction")
st.markdown("""
### Pressure Levels:
- **No**: No parental pressure[0].
- **Low**: Slight pressure with minimal impact[1].
- **Medium**: Moderate pressure with noticeable impact[2].
- **High**: Significant pressure affecting your well-being[3].
- **Very High**: Severe pressure causing considerable stress and anxiety[4].
""")

st.markdown("Please answer the following questions based on your experiences:")

questions = [
    "1. Do you feel that your parents have high expectations regarding your academic performance?",
    "2. How often do your parents compare your achievements with those of other students?",
    "3. Do you feel stressed or anxious when discussing your grades with your parents?",
    "4. Have your parents ever set specific grade targets for you to achieve?",
    "5. Do you feel pressured to choose a particular career path because of your parents’ expectations?",
    "6. How do your parents react when you do not meet their academic expectations?",
    "7. Have your parents enrolled you in extra coaching or tuition classes without your choice?",
    "8. Do you feel guilty or ashamed when you fail to meet your parents’ expectations?",
    "9. Have you ever felt that your parents’ expectations negatively impact your mental well-being?",
    "10. Do you hesitate to express your academic struggles to your parents for fear of disappointment?",
    "11. Have your parents ever discouraged you from engaging in hobbies or extracurricular activities to focus on studies?",
    "12. How often do your parents compare your performance with that of your siblings or relatives?",
    "13. Do your parents expect you to follow in their footsteps in terms of career or life choices?",
    "14. Do you feel that you have the freedom to make your own academic and career decisions?",
    "15. Have your parents ever forced you to study a subject or take a course against your interests?"
]

answers = []
for q in questions:
    response = st.selectbox(q, list(options.keys()))
    answers.append(options[response])

# Prediction
if st.button("Predict Pressure Level"):
    pressure_level = predict_pressure(answers)
    st.success(f"Predicted Parental Pressure Level: {[pressure_level]}")
