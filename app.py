# 🎓 Student Welfare Data Analysis using NumPy, Pandas, and Streamlit

import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------
# App Title
# -------------------------------
st.set_page_config(page_title="Student Welfare Data Analysis", layout="wide")
st.title("🎓 Student Welfare Data Analysis")
st.markdown("Analyze and improve student performance using **NumPy** and **Pandas**!")

# -------------------------------
# Step 1: Create dummy student data
# -------------------------------
np.random.seed(10)

names = ['Aarav', 'Riya', 'Kabir', 'Saanvi', 'Arjun', 'Meera', 'Dev', 'Isha', 'Rohan', 'Diya']
n = len(names)

data = {
    'Name': names,
    'Math': np.random.randint(40, 100, n),
    'Science': np.random.randint(35, 100, n),
    'English': np.random.randint(45, 100, n),
    'Attendance (%)': np.random.randint(50, 100, n),
    'Activity_Points': np.random.randint(10, 50, n)
}

df = pd.DataFrame(data)

st.subheader("📋 Student Data")
st.dataframe(df, use_container_width=True)

# -------------------------------
# Step 2: Compute totals and averages
# -------------------------------
df['Total Marks'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Average Marks'] = np.round(df[['Math', 'Science', 'English']].mean(axis=1), 2)

# -------------------------------
# Step 3: Classify welfare status
# -------------------------------
def welfare_status(row):
    if row['Average Marks'] < 50 or row['Attendance (%)'] < 60:
        return 'Needs Support'
    elif row['Average Marks'] >= 80 and row['Attendance (%)'] >= 85:
        return 'Excellent'
    else:
        return 'Good'

df['Welfare_Status'] = df.apply(welfare_status, axis=1)

# -------------------------------
# Step 4: Summary analysis
# -------------------------------
total_students = len(df)
excellent_count = (df['Welfare_Status'] == 'Excellent').sum()
support_count = (df['Welfare_Status'] == 'Needs Support').sum()
correlation = df['Attendance (%)'].corr(df['Average Marks'])

# -------------------------------
# Step 5: Display results
# -------------------------------
st.subheader("📊 Student Welfare Analysis Report")
st.dataframe(df[['Name', 'Average Marks', 'Attendance (%)', 'Welfare_Status']], use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Students", total_students)
col2.metric("Excellent Students", excellent_count)
col3.metric("Needs Support", support_count)
col4.metric("Attendance–Marks Correlation", f"{correlation:.2f}")

# -------------------------------
# Step 6: Data visualization
# -------------------------------
st.subheader("📈 Data Visualization")

chart_option = st.selectbox("Select a chart to view:", ["Average Marks", "Attendance (%)", "Activity_Points"])

st.bar_chart(df.set_index('Name')[chart_option])

# -------------------------------
# Step 7: Download report
# -------------------------------
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download CSV Report",
    data=csv,
    file_name='student_welfare_report.csv',
    mime='text/csv'
)
st.success("✅ Report ready for download!")

st.caption("Developed using Python, NumPy, Pandas, and Streamlit for student welfare analysis.")
