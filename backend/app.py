# File: streamlit_app.py

import streamlit as st
import requests
import os
import plotly.express as px
from dotenv import load_dotenv
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import datetime
import json

# Load API keys from .env
load_dotenv()
API_KEY = os.getenv('CALORIE_NINJAS_API_KEY')
STRIPE_PREMIUM_URL = "https://buy.stripe.com/test_xxx"  # Replace with real Stripe URL

# Set Streamlit config
st.set_page_config(page_title="NutriSmart AI", layout="wide", initial_sidebar_state="expanded")

# Initialize session state for meal history and calorie goals
if 'meal_history' not in st.session_state:
    st.session_state.meal_history = []
if 'calorie_goal' not in st.session_state:
    st.session_state.calorie_goal = None
if 'health_tips' not in st.session_state:
    st.session_state.health_tips = [
        "Stay hydrated by drinking at least 8 glasses of water daily!",
        "Incorporate a variety of colorful vegetables for balanced nutrition.",
        "Aim for 150 minutes of moderate exercise per week."
    ]

# --- Navigation Menu using streamlit_option_menu ---
with st.sidebar:
    st.image("https://i.ibb.co/yNJw2Sc/nutri-logo.png", width=180)
    st.markdown("**NutriSmart AI**")
    st.markdown("All-in-one meal analyzer, BMI tracker, and health advisor.")
    st.markdown("---")

    # Stylish horizontal or vertical menu
    selected = option_menu(
        menu_title=None,
        options=["Meal Analyzer", "BMI Calculator", "Meal History", "Calorie Goal", "Health Tips", "Premium"],
        icons=["egg-fried", "calculator", "book", "target", "lightbulb", "gem"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",  # Change to "horizontal" for a different look
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "#ff4b4b", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#ff4b4b"},
        }
    )
    st.markdown("Built with ❤️ using Streamlit")

# Main app title
st.title("🍽️ NutriSmart AI")
st.caption("_Your personalized health & nutrition dashboard_ ✨")

# --- Meal Analyzer ---
if selected == "Meal Analyzer":
    st.subheader("🥗 Analyze Your Meal")
    col1, col2 = st.columns([3, 1])
    with col1:
        meal_input = st.text_area("Describe your meal (e.g., 2 boiled eggs and toast with butter)", height=100)
    with col2:
        st.markdown("**Quick Tips**")
        st.write("- Be specific (e.g., '100g grilled chicken' vs 'chicken').")
        st.write("- Include portion sizes for accurate results.")
        st.write("- Separate items with commas or 'and'.")

    if st.button("🔍 Analyze Meal"):
        if meal_input:
            with st.spinner("Calling CalorieNinjas API..."):
                headers = {"X-Api-Key": API_KEY}
                url = f"https://api.calorieninjas.com/v1/nutrition?query={meal_input}"
                response = requests.get(url, headers=headers)

                if response.status_code == 200:
                    data = response.json()
                    items = data['items']
                    if not items:
                        st.warning("No nutrition data found. Try a more detailed description.")
                    else:
                        st.success("✅ Meal analyzed successfully!")
                        st.write("### 🍱 Meal Breakdown:")
                        st.dataframe(items)

                        # Totals
                        total = {"protein": 0, "fat": 0, "carbs": 0, "calories": 0}
                        for item in items:
                            total["protein"] += item.get("protein_g", 0)
                            total["fat"] += item.get("fat_total_g", 0)
                            total["carbs"] += item.get("carbohydrates_total_g", 0)
                            total["calories"] += item.get("calories", 0)

                        # Save to meal history
                        meal_entry = {
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "meal": meal_input,
                            "calories": total["calories"],
                            "protein": total["protein"],
                            "fat": total["fat"],
                            "carbs": total["carbs"]
                        }
                        st.session_state.meal_history.append(meal_entry)

                        # Pie Chart
                        fig = px.pie(
                            names=["Protein", "Fat", "Carbs"],
                            values=[total["protein"], total["fat"], total["carbs"]],
                            title=f"🍽️ Macronutrient Breakdown (Total Calories: {int(total['calories'])})",
                            color_discrete_sequence=px.colors.sequential.Viridis
                        )
                        st.plotly_chart(fig, use_container_width=True)

                        # Progress towards calorie goal
                        if st.session_state.calorie_goal:
                            progress = (total["calories"] / st.session_state.calorie_goal) * 100
                            st.progress(min(progress / 100, 1.0))
                            st.write(f"Consumed {int(total['calories'])} of {st.session_state.calorie_goal} daily calories ({progress:.1f}%)")
                else:
                    st.error("❌ API request failed.")
        else:
            st.warning("Please enter a meal description first.")

# --- BMI Calculator ---
elif selected == "BMI Calculator":
    st.subheader("⚖️ BMI Calculator")
    col1, col2 = st.columns(2)

    with col1:
        weight = st.number_input("Enter your weight (kg)", min_value=1.0, value=60.0)
    with col2:
        height = st.number_input("Enter your height (cm)", min_value=1.0, value=170.0)

    if st.button("📏 Calculate BMI"):
        try:
            height_m = height / 100
            bmi = weight / (height_m ** 2)
            st.metric(label="Your BMI", value=round(bmi, 2))

            # BMI Category with additional advice
            if bmi < 18.5:
                st.info("You are underweight. Consider consulting a dietitian to ensure balanced nutrition.")
            elif 18.5 <= bmi < 25:
                st.success("You have a normal weight. Keep maintaining a healthy lifestyle!")
            elif 25 <= bmi < 30:
                st.warning("You are overweight. Regular exercise and portion control can help.")
            else:
                st.error("You are obese. A healthcare provider can guide you toward healthy weight loss.")
        except:
            st.error("Invalid input. Please check values.")

# --- Meal History ---
elif selected == "Meal History":
    st.subheader("📚 Meal History")
    if st.session_state.meal_history:
        df = pd.DataFrame(st.session_state.meal_history)
        st.dataframe(df, use_container_width=True)

        # Download history as CSV
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Meal History",
            data=csv,
            file_name="meal_history.csv",
            mime="text/csv"
        )

        # Clear history
        if st.button("🗑️ Clear History"):
            st.session_state.meal_history = []
            st.experimental_rerun()
    else:
        st.info("No meals logged yet. Analyze a meal to start tracking!")

    # Simple trend chart
    if len(st.session_state.meal_history) > 1:
        df = pd.DataFrame(st.session_state.meal_history)
        fig = px.line(df, x="date", y="calories", title="Calorie Intake Over Time", markers=True)
        st.plotly_chart(fig, use_container_width=True)

# --- Calorie Goal Planner ---
elif selected == "Calorie Goal":
    st.subheader("🎯 Set Daily Calorie Goal")
    calorie_goal = st.number_input("Enter your daily calorie goal", min_value=500, value=2000, step=100)
    if st.button("💾 Save Goal"):
        st.session_state.calorie_goal = calorie_goal
        st.success(f"Daily calorie goal set to {calorie_goal} calories!")

    if st.session_state.calorie_goal:
        st.metric("Current Calorie Goal", f"{st.session_state.calorie_goal} kcal")
        # Calculate total calories consumed today
        today = datetime.now().strftime("%Y-%m-%d")
        today_meals = [m for m in st.session_state.meal_history if m["date"].startswith(today)]
        total_today = sum(m["calories"] for m in today_meals)
        st.write(f"Calories consumed today: {int(total_today)} kcal")
        progress = (total_today / st.session_state.calorie_goal) * 100
        st.progress(min(progress / 100, 1.0))
        st.write(f"Progress: {progress:.1f}% of daily goal")

# --- Health Tips ---
elif selected == "Health Tips":
    st.subheader("💡 AI-Powered Health Tips")
    st.write("Get personalized health and nutrition advice!")
    for tip in st.session_state.health_tips:
        st.markdown(f"- {tip}")
    
    # Add custom tip
    new_tip = st.text_input("Add your own health tip:")
    if st.button("➕ Add Tip"):
        if new_tip:
            st.session_state.health_tips.append(new_tip)
            st.success("Tip added!")
            st.experimental_rerun()

# --- Premium Access ---
elif selected == "Premium":
    st.subheader("💎 Premium Access")
    st.write("Upgrade to premium to unlock personalized meal tracking, AI suggestions, and SMS health reminders!")
    st.markdown(f"[🚀 Upgrade via Stripe]({STRIPE_PREMIUM_URL})", unsafe_allow_html=True)
    st.write("**Premium Features Include:**")
    st.markdown("""
    - 📊 Advanced meal tracking with weekly/monthly analytics
    - 🤖 AI-driven meal suggestions based on your goals
    - 📱 SMS reminders for meals and hydration
    - 🥗 Custom recipe generator
    """)

# Footer
st.markdown("---")
st.caption("© 2025 NutriSmart AI. All rights reserved.")