# E-CELL – Virtual Electrochemistry Lab

A Streamlit-based virtual engineering chemistry laboratory.

## Features
- Galvanic Cell simulator
- Nernst Equation calculator
- Gibbs Free Energy calculator
- Theory module
- Quiz
- Automatic PDF report generation

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Upload all files to a GitHub repository.
2. Open Streamlit Community Cloud.
3. Select the repository and `app.py`.
4. Deploy.

The report generator uses ReportLab and creates the PDF directly in the browser session.
