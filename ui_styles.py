def get_ui_styles():
    return """
    <style>
        .stApp {
            background-color: #0b1220;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        h1 {
            color: #e5edf8;
            font-weight: 750;
            letter-spacing: 0.5px;
        }

        h3 {
            color: #dbeafe;
            font-weight: 650;
            margin-top: 2rem;
        }

        div[data-testid="stMetric"] {
            background-color: #111c2e;
            border: 1px solid #263650;
            border-radius: 10px;
            padding: 14px 16px;
        }

        div[data-testid="stMetricLabel"] {
            color: #9fb0c8;
        }

        div[data-testid="stMetricValue"] {
            color: #f8fafc;
        }

        div.stButton > button {
            background-color: #2563eb;
            color: white;
            border: 1px solid #3b82f6;
            border-radius: 7px;
            font-weight: 600;
            padding: 0.45rem 1rem;
        }

        div.stButton > button:hover {
            background-color: #1d4ed8;
            color: white;
            border-color: #60a5fa;
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid #263650;
            border-radius: 8px;
            overflow: hidden;
        }
    </style>
    """