# Streamlit Multi-Page Dashboard

This project is a beginner-friendly, interactive multi-page web app built using [Streamlit](https://streamlit.io/). It allows you to:

- Upload and explore CSV files
- Visualize column data with charts
- Use a clean multi-page layout (Home, Data Explorer, Charts)
- Deploy instantly using Streamlit Cloud

## 🚀 Features

- CSV File Upload
- Data Preview Table
- Bar Chart Visualization
- Multi-Page Navigation
- Lightweight and fast

## 📁 Folder Structure

streamlit-multipage-dashboard/
├── app.py
├── pages/
│ ├── 1_Data_Explorer.py
│ └── 2_Charts.py
├── requirements.txt


## 🧪 Run Locally

```bash
git clone https://github.com/your-username/streamlit-multipage-dashboard.git
cd streamlit-multipage-dashboard
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
