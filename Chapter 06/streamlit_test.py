import streamlit as st
import pandas as pd
import numpy as np
from fpdf import FPDF
from io import BytesIO

# Function to load data
def load_data(file):
    return pd.read_csv(file)

# Function to generate PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Bank Data Report', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_table(self, data, title):
        self.add_page()
        self.chapter_title(title)
        self.set_font('Arial', '', 12)
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.cell(40, 10, str(data[i][j]), 1, 0, 'C')
            self.ln()

def export_pdf(dataframe):
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title('Summary Statistics')
    pdf.chapter_body(dataframe.describe().to_string())

    data = dataframe.values.tolist()
    pdf.add_table(data, 'Data')

    # Save PDF to BytesIO object
    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer.getvalue()

# Title of the dashboard
st.title("Bank Data Dashboard")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = load_data(uploaded_file)

    # Display raw data
    st.header("Raw Data")
    st.write(df)

    # Summary statistics
    st.header("Summary Statistics")
    st.write(df.describe())

    # Line chart for the "income" column
    st.header("Income Line Chart")
    st.line_chart(df["income"])

    # Histogram for the "income" column
    st.header("Income Distribution")
    st.bar_chart(np.histogram(df["income"], bins=30)[0])

    # Pie chart for the "pep" column (yes/no)
    st.header("PEP Distribution")
    pep_counts = df['pep'].value_counts()
    st.write(pep_counts)
    st.pyplot(pep_counts.plot.pie(autopct="%1.1f%%").figure)

    # Scatter plot for "income" vs "age"
    st.header("Income vs Age Scatter Plot")
    st.write(df.plot.scatter(x='age', y='income'))

    # Additional options
    st.sidebar.header("Options")

    # Filter data based on age
    age_filter = st.sidebar.slider('Filter by Age', min_value=int(df['age'].min()), max_value=int(df['age'].max()),
                                   value=(int(df['age'].min()), int(df['age'].max())))
    filtered_data = df[(df['age'] >= age_filter[0]) & (df['age'] <= age_filter[1])]

    st.subheader(f"Data filtered by age between {age_filter[0]} and {age_filter[1]}")
    st.write(filtered_data)

    # Filter data based on income
    income_filter = st.sidebar.slider('Filter by Income', min_value=int(df['income'].min()),
                                      max_value=int(df['income'].max()),
                                      value=(int(df['income'].min()), int(df['income'].max())))
    filtered_data_income = df[(df['income'] >= income_filter[0]) & (df['income'] <= income_filter[1])]

    st.subheader(f"Data filtered by income between {income_filter[0]} and {income_filter[1]}")
    st.write(filtered_data_income)

    # Button to export PDF
    if st.button('Export as PDF'):
        pdf_bytes = export_pdf(df)
        st.download_button(label="Download PDF", data=pdf_bytes, file_name="bank_data_report.pdf",
                           mime="application/pdf")
else:
    st.write("Please upload a CSV file to proceed.")
