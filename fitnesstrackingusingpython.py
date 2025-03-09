import streamlit as st
import pandas as pd
import plotly.express as px

# Function to calculate BMI
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

# Function to calculate BMR
def calculate_bmr(weight, height, age, gender):
    if gender == 'Male':
        return round(88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age), 2)
    else:
        return round(447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age), 2)

# Function to calculate calories burned
def calculate_calories_burned(weight, activity_level):
    activity_multiplier = {'Sedentary': 1.2, 'Lightly Active': 1.375, 'Moderately Active': 1.55, 'Very Active': 1.725}
    return round(weight * activity_multiplier[activity_level] * 10, 2)

# Streamlit App Configuration
st.set_page_config(page_title="Fitness Tracker", page_icon="💪", layout="centered")
st.title("🏋️ Fitness Tracking App")

# User Input Section
st.sidebar.header("User Input")
weight = st.sidebar.number_input("Enter your weight (kg)", min_value=10.0, max_value=200.0, step=0.1)
height = st.sidebar.number_input("Enter your height (m)", min_value=0.5, max_value=2.5, step=0.01)
age = st.sidebar.number_input("Enter your age", min_value=5, max_value=100, step=1)
gender = st.sidebar.selectbox("Select Gender", ['Male', 'Female'])
activity_level = st.sidebar.selectbox("Activity Level", ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active'])
goal = st.sidebar.selectbox("Fitness Goal", ['Weight Loss', 'Muscle Gain', 'Maintain Fitness'])
workout_type = st.sidebar.selectbox("Workout Type", ['Cardio', 'Strength Training', 'Flexibility', 'Mixed'])
workout_duration = st.sidebar.slider("Workout Duration (minutes)", 0, 180, 30)
sleep_duration = st.sidebar.slider("Sleep Duration (hours)", 0, 12, 7)
nutrients_intake = st.sidebar.slider("Daily Nutrients Intake (Calories)", 1000, 5000, 2000)

if st.sidebar.button("Calculate"):
    bmi = calculate_bmi(weight, height)
    bmr = calculate_bmr(weight, height, age, gender)
    calories_burned = calculate_calories_burned(weight, activity_level)
    
    st.success("✅ Calculations Completed!")
    st.markdown(f"**📊 Your BMI:** `{bmi}`")
    st.markdown(f"**🔥 Your BMR:** `{bmr}` kcal/day")
    st.markdown(f"**🏃 Calories Burned (Daily Estimate):** `{calories_burned}` kcal")
    st.markdown(f"**💪 Workout Type:** `{workout_type}` for `{workout_duration}` minutes")
    st.markdown(f"**🌙 Sleep Duration:** `{sleep_duration}` hours")
    st.markdown(f"**🥗 Nutrients Intake:** `{nutrients_intake}` kcal/day")
    
    if bmi < 18.5:
        st.warning("⚠️ You are underweight. Consider a balanced diet!")
    elif bmi < 24.9:
        st.success("✅ You have a normal weight. Keep it up!")
    elif bmi < 29.9:
        st.warning("⚠️ You are overweight. Consider regular exercise!")
    else:
        st.error("🚨 You are obese. Consult a healthcare provider!")

    # Data visualization
    data = pd.DataFrame({
        'Metrics': ['BMI', 'BMR', 'Calories Burned', 'Workout Duration', 'Sleep Duration', 'Nutrient Intake'],
        'Values': [bmi, bmr, calories_burned, workout_duration, sleep_duration, nutrients_intake]
    })
    
    fig = px.bar(data, x='Metrics', y='Values', color='Metrics', title="Health Metrics Overview")
    st.plotly_chart(fig)

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tip:** Stay active and maintain a balanced diet for a healthy lifestyle!")