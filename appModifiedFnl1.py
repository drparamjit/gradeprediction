# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 21:37:18 2025

@author: Dr Paramjit Singh
"""


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Model training data
# Columns: [Hours Studied Daily, Past Score, Attendance, Sleep Hours Daily, Sleep Hours Daily^2]
# Revised training data to ensure:
# 1. Higher 'Hours Studied Daily' generally leads to higher grades.
# 2. Higher 'Attendance' generally leads to higher grades.
# 3. 'Sleep Hours Daily' has an optimal effect (using a quadratic term):
#    - Too little sleep leads to lower grades.
#    - Optimal sleep leads to higher grades.
#    - Too much sleep might plateau or slightly decrease grades.

# Original features: [Hours Studied Daily, Past Score, Attendance, Sleep Hours Daily]
X_original = np.array([
    [1, 30, 10, 4],  # Very low hours, past score, attendance, low sleep -> very low grade
    [2, 50, 40, 5],  # Low hours, past score, attendance, low sleep -> low grade
    [3, 60, 65, 6],  # Moderate sleep, better grade
    [4, 55, 70, 7],  # Optimal sleep range
    [5, 70, 80, 8],  # Optimal sleep range, higher grade
    [6, 75, 85, 7],  # Optimal sleep range
    [7, 80, 90, 6],  # Lower sleep hours, might see a slight dip if other factors are high
    [8, 85, 95, 8],  # Very high hours, very high attendance, optimal sleep -> very high grade
    [9, 90, 98, 9]    # Excellent hours, excellent attendance, slightly more sleep -> near perfect grade
])

# Grades corresponding to the X_original data
y = np.array([30, 45, 60, 75, 85, 88, 82, 95, 98]) # Adjusted y to reflect impact of hours, attendance, and sleep

# Create PolynomialFeatures to add the quadratic term for Sleep Hours Daily
# We'll apply this to the Sleep Hours column specifically, or let PolynomialFeatures do it for all.
# For simplicity, let's just manually add the sleep_hours^2 for training.
# In a real scenario, you'd use PolynomialFeatures for automatic generation.

# Let's manually create the X matrix with the squared sleep term for demonstration
# X = [Hours, Past, Attn, Sleep, Sleep^2]
X = np.hstack((X_original, (X_original[:, 3]**2).reshape(-1, 1)))

# Train the Linear Regression model
model = LinearRegression().fit(X, y)

# Define feedback and grading logic
def get_feedback(grade):
    if grade >= 90:
        return "🌟 Excellent! Keep up the great work!", "A+"
    elif grade >= 80:
        return "👍 Very Good! You're on the right track!", "A"
    elif grade >= 70:
        return "🙂 Good! A bit more effort and you'll shine!", "B"
    elif grade >= 60:
        return "😐 Fair. Try to focus and revise regularly.", "C"
    else:
        return "⚠️ Needs Improvement. Consider a better routine.", "D"

# Web UI

st.markdown("#### 📚 Academic Grade Optimizer")
# Add the author name and horizontal line
#st.markdown("Author: Dr Paramjit Singh")
st.caption("Author: Dr Paramjit Singh")
#st.write("---")
st.divider() # This creates a horizontal line



# Custom CSS to change the color of the horizontal line
st.markdown("""
    <style>
    hr {
        border-top: 1px outset grey; /* Example: orange-red color, adjust as needed */
        margin-top: 5px;
        margin-bottom: 2px;
    }
    </style>
""", unsafe_allow_html=True)



st.markdown("Enter below your academic and lifestyle details to predict your final exam score:")

# Input sliders - Using columns to place sliders in the same line as their labels
# Note: Streamlit sliders inherently have their label above them within the widget itself.
# To make them appear "in the same line as their label" likely means placing the *entire slider widget* side-by-side.
# We'll create columns for each slider to achieve this horizontal layout.

col1, col2 = st.columns(2)
with col1:
    hours = st.slider("Hours Studied Daily", 0, 10, 5)
with col2:
    past = st.slider("Past Score (%)", 0, 100, 60)

col3, col4 = st.columns(2)
with col3:
    attn = st.slider("Attendance (%)", 0, 100, 80)
with col4:
    sleep = st.slider("Sleep Hours Daily", 0, 12, 7)

# Prediction and feedback
if st.button("Predict Grade"):
    # Prepare input data, including the squared sleep term
    input_data = np.array([[hours, past, attn, sleep, sleep**2]])
    grade = model.predict(input_data)[0]

    # SOLUTION: Clip the predicted grade to be between 0 and 100%
    # This prevents grades like 101% or negative grades.
    grade = max(0, min(100, grade))

    feedback, grade_letter = get_feedback(grade)

    #st.subheader(f"🎯 Predicted Final Grade: `{grade:.2f}%` ({grade_letter})")
    st.divider() # This creates a horizontal line
    st.markdown(f"#### ✏️ Predicted Final Grade: `{grade:.2f}%` ({grade_letter})")
    st.markdown(f"**Feedback:** {feedback}")

    # Chart - Simulate comparison
    #fig, ax = plt.subplots()
    #fig, ax = plt.subplots(figsize=(8, 5)) # Changed figure size here
    #fig, ax = plt.subplots(figsize=(3, 2)) # Changed figure size here
    fig, ax = plt.subplots(figsize=(3, 2)) # Changed figure size here
    categories = ['Predicted Grade', 'Past Score', 'Ideal Target']
    values = [grade, past, 90]
    #bars = ax.bar(categories, values, color=['red', 'blue', 'green'], width=0.5) # Bar width adjustment here
    bars = ax.bar(categories, values, color=['teal', 'olive', 'purple'], width=0.5) # Bar width adjustment here
    # May try any of theses colors: 'red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 
    #'white', 'orange', 'purple', 'brown', 'pink', 'gray', 'lime', 'teal', 'maroon', 'navy', 'olive', 'aqua'.
    
    
    
    #bars = ax.bar(categories, values, color=['red', 'blue', 'green'])
    ax.set_ylim([0, 100])
    
    
    # Set X and Y axis labels for decency
    ax.set_xlabel("Metric", fontsize=6)
    ax.set_ylabel("Value (%)", fontsize=6)

    # Corrected: Adjusted font size of x-axis and y-axis tick labels
    ax.tick_params(axis='x', labelsize=5) # Reduce x-axis tick label font size
    ax.tick_params(axis='y', labelsize=5) # Reduce y-axis tick label font size


    
    
    for bar in bars:
        height = bar.get_height()
        
        # Corrected: Adjusted font size of labels on the bars
        ax.annotate(f'{height:.0f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=5) # Font size adjustment here

        
        #ax.annotate(f'{height:.0f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                    #xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')
    st.pyplot(fig)