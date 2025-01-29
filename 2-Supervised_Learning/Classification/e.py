from fpdf import FPDF

# Create a PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Content for the PDF
pdf_content = """
Logistic Regression Overview

Logistic regression is a widely used method for binary classification. It predicts the probability 
of a given sample belonging to one of two classes. This document provides a high-level overview of how logistic regression works.

Steps Involved:

1. Input Data:
- Features (X): A matrix of input variables, where each row represents a sample and each column represents a feature.
- Target (Y): Binary values indicating the class (0 or 1).

2. Linear Combination:
Logistic regression first computes a linear combination of the input features:
z = weight * feature + bias

3. Sigmoid Function:
The linear output z is transformed into a probability value using the sigmoid function:
sigmoid(z) = 1 / (1 + exp(-z))

4. Classification:
- If the probability is greater than or equal to 0.5, the sample is classified as Class 2 (Y = 1).
- If the probability is less than 0.5, the sample is classified as Class 1 (Y = 0).

5. Loss Function:
The model minimizes the log-loss function to improve its predictions:
Loss = - (y * log(predicted) + (1 - y) * log(1 - predicted))

Key Points:
- Logistic regression combines linear models with a sigmoid function to predict probabilities.
- It is efficient, interpretable, and commonly used for binary classification problems.

Example Applications:
- Email spam detection (Spam vs. Not Spam).
- Medical diagnosis (Disease vs. No Disease).
- Credit scoring (Default vs. No Default).

Why Use Logistic Regression?
- Simple to implement and interpret.
- Effective for linearly separable data.
- Can handle multiple input features.

This is a quick introduction to logistic regression. For more in-depth understanding, explore resources like academic articles or advanced machine learning textbooks.
"""

# Add content to the PDF
for line in pdf_content.split("\n"):
    pdf.cell(0, 10, txt=line, ln=True)

# Save the PDF
pdf_file_path = "/mnt/data/Logistic_Regression_Overview.pdf"
pdf.output(pdf_file_path)

pdf_file_path
