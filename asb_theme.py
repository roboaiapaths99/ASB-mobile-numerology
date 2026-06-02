import streamlit as st

def apply_asb_theme():
    """Apply ASB Reports inspired theme to Streamlit app"""
    
    # Custom CSS based on ASB Reports theme
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&family=Cinzel:wght@400;700&family=Outfit:wght@300;400;600&display=swap');
    
    :root {
        --asb-purple: #8b5cf6;
        --asb-magenta: #d946ef;
        --asb-gold: #d4af37;
        --asb-text: #1e1b4b;
        --asb-surface: #fff;
        --asb-bg: #fdf8f4;
        --gradient-accent: linear-gradient(90deg, #8b5cf6, #d946ef);
    }
    
    body {
        --tw-bg-opacity: 1;
        --tw-text-opacity: 1;
        background-color: #fdf8f4;
        background-color: rgb(253 248 244 / var(--tw-bg-opacity, 1));
        color: #1e1b4b;
        color: rgb(30 27 75 / var(--tw-text-opacity, 1));
        font-family: 'Inter', system-ui, sans-serif;
        margin: 0;
        min-height: 100vh;
        overflow-x: hidden;
        padding: 0;
    }
    
    body::before {
        background-image: linear-gradient(#d4af370d 1px, #0000 0), linear-gradient(90deg, #d4af370d 1px, #0000 0);
        background-size: 80px 80px;
        content: "";
        height: 100%;
        left: 0;
        pointer-events: none;
        position: fixed;
        top: 0;
        width: 100%;
        z-index: -1;
    }
    
    /* Streamlit specific overrides */
    .stApp {
        background-color: #fdf8f4 !important;
        font-family: 'Inter', system-ui, sans-serif !important;
    }
    
    .stMarkdown {
        font-family: 'Inter', system-ui, sans-serif !important;
    }
    
    /* Headers with Cinzel font */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Cinzel', serif !important;
        color: #1e1b4b !important;
    }
    
    /* Main container */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    /* ASB Button Style */
    .asb-button {
        background: linear-gradient(90deg, #8b5cf6, #d946ef);
        background: var(--gradient-accent);
        box-shadow: 0 10px 20px -5px #8b5cf64d;
        color: #fff;
        transition: all 0.3s ease;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 0.75rem;
        font-weight: 600;
        cursor: pointer;
        font-family: 'Inter', system-ui, sans-serif;
    }
    
    .asb-button:hover {
        box-shadow: 0 15px 30px -5px #8b5cf666;
        transform: translateY(-2px);
    }
    
    /* ASB Gold Button */
    .asb-button-gold {
        background: linear-gradient(135deg, #fce08e, #d4af37);
        color: #fff;
        box-shadow: 0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 0.75rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        font-family: 'Inter', system-ui, sans-serif;
    }
    
    .asb-button-gold:hover {
        transform: translateY(-2px);
        box-shadow: 0 25px 50px -12px #00000040;
        opacity: 0.9;
    }
    
    /* ASB Card Style */
    .asb-card {
        background: #fff;
        border-radius: 2rem;
        border: 1px solid #d4af3733;
        box-shadow: 0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        padding: 2rem;
    }
    
    .asb-card:hover {
        border-color: #8b5cf633;
        box-shadow: 0 20px 40px -20px #8b5cf633;
        transform: translateY(-8px);
    }
    
    /* Glass Effect */
    .glass {
        background: #ffffffb3;
        border: 1px solid #fff;
        border-radius: 2rem;
        box-shadow: 0 20px 25px -5px #0000001a, 0 8px 10px -6px #0000001a;
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
    }
    
    /* Gradient Text */
    .asb-gradient-text {
        background: linear-gradient(to right, #d4af37, #d946ef, #8b5cf6);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-family: 'Cinzel', serif;
        font-weight: 700;
    }
    
    /* Mystic Border */
    .mystic-border {
        border: 1px solid #d4af37;
        border-opacity: 0.3;
        position: relative;
        border-radius: 1rem;
    }
    
    .mystic-border::after {
        background: linear-gradient(to right, #d4af37, #d946ef);
        border-radius: 1rem;
        content: "";
        filter: blur(8px);
        inset: -0.125rem;
        opacity: 0;
        pointer-events: none;
        position: absolute;
        transition: all 0.5s ease;
    }
    
    .mystic-border:hover::after {
        opacity: 0.2;
    }
    
    /* Input Fields */
    .stTextInput > div > div > input {
        background: #fff !important;
        border: 1px solid #d4af37 !important;
        border-radius: 0.75rem !important;
        padding: 0.75rem 1rem !important;
        font-family: 'Inter', system-ui, sans-serif !important;
        color: #1e1b4b !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 2px #8b5cf633 !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #8b5cf6, #d946ef) !important;
        border: none !important;
        border-radius: 0.75rem !important;
        color: #fff !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        font-family: 'Inter', system-ui, sans-serif !important;
    }
    
    .stButton > button:hover {
        box-shadow: 0 15px 30px -5px #8b5cf666 !important;
        transform: translateY(-2px) !important;
    }
    
    /* DataFrames */
    .stDataFrame {
        background: #fff !important;
        border-radius: 1rem !important;
        border: 1px solid #d4af3733 !important;
        overflow: hidden !important;
    }
    
    .stDataFrame table {
        border-collapse: collapse !important;
        width: 100% !important;
    }
    
    .stDataFrame th {
        background: linear-gradient(90deg, #8b5cf6, #d946ef) !important;
        color: #fff !important;
        font-family: 'Cinzel', serif !important;
        font-weight: 600 !important;
        padding: 1rem !important;
        text-align: center !important;
    }
    
    .stDataFrame td {
        padding: 0.75rem 1rem !important;
        border-bottom: 1px solid #d4af371a !important;
        font-family: 'Inter', system-ui, sans-serif !important;
    }
    
    /* Success/Good rows */
    .stDataFrame tr[data-testid="stDataFrame"] td:first-child:contains("Good") {
        background-color: #e6f7ed !important;
        color: #2d5a3d !important;
        font-weight: 600 !important;
    }
    
    /* Error/Bad rows */
    .stDataFrame tr[data-testid="stDataFrame"] td:first-child:contains("Bad") {
        background-color: #ffe8e0 !important;
        color: #8b4513 !important;
        font-weight: 600 !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background-color: #fdf8f4;
    }
    
    ::-webkit-scrollbar-thumb {
        background-color: #d4af37;
        border-radius: 9999px;
        opacity: 0.4;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        opacity: 1;
    }
    
    /* Section titles */
    .section-title {
        font-family: 'Cinzel', serif !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #1e1b4b !important;
        margin: 2rem 0 1rem 0 !important;
        text-align: center !important;
        background: linear-gradient(90deg, #d4af37, #d946ef, #8b5cf6);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }
    
    /* Result cards */
    .result-card {
        background: #fff !important;
        border: 1px solid #d4af3733 !important;
        border-radius: 1.5rem !important;
        padding: 1.5rem !important;
        box-shadow: 0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a !important;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
        margin-bottom: 1rem !important;
    }
    
    .result-card:hover {
        border-color: #8b5cf633 !important;
        box-shadow: 0 20px 40px -20px #8b5cf633 !important;
        transform: translateY(-4px) !important;
    }
    
    .result-card h4 {
        font-family: 'Cinzel', serif !important;
        color: #1e1b4b !important;
        margin-bottom: 0.5rem !important;
        font-size: 1.25rem !important;
    }
    
    .result-card p {
        color: #64748b !important;
        font-family: 'Inter', system-ui, sans-serif !important;
        margin: 0 !important;
    }
    
    /* Metric boxes */
    .metric-box {
        background: #fff !important;
        border: 1px solid #d4af3733 !important;
        border-radius: 1rem !important;
        padding: 1.5rem !important;
        text-align: center !important;
        box-shadow: 0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a !important;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
    }
    
    .metric-box:hover {
        border-color: #8b5cf633 !important;
        box-shadow: 0 20px 40px -20px #8b5cf633 !important;
        transform: translateY(-4px) !important;
    }
    
    .metric-box.gold {
        background: linear-gradient(135deg, #fce08e, #d4af37) !important;
        color: #fff !important;
        border: none !important;
    }
    
    .metric-box.green {
        background: linear-gradient(135deg, #86efac, #22c55e) !important;
        color: #fff !important;
        border: none !important;
    }
    
    .metric-box h3 {
        font-family: 'Cinzel', serif !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }
    
    .metric-box p {
        font-family: 'Inter', system-ui, sans-serif !important;
        margin: 0.5rem 0 0 0 !important;
        opacity: 0.9 !important;
    }
    
    /* Links */
    a {
        color: #8b5cf6 !important;
        text-decoration: none !important;
        transition: all 0.3s ease !important;
    }
    
    a:hover {
        color: #d946ef !important;
        text-decoration: underline !important;
    }
    
    /* Error messages */
    .error-banner {
        background: #fef2f2 !important;
        border: 1px solid #ef444433 !important;
        border-radius: 0.75rem !important;
        padding: 1rem !important;
        color: #dc2626 !important;
        font-family: 'Inter', system-ui, sans-serif !important;
        margin-bottom: 1rem !important;
    }
    
    /* Animations */
    @keyframes cosmic-float {
        0%, 100% {
            transform: translateY(0) rotate(0);
        }
        50% {
            transform: translateY(-15px) rotate(2deg);
        }
    }
    
    .cosmic-float {
        animation: cosmic-float 6s ease-in-out infinite;
    }
    
    .number-glow {
        text-shadow: 0 0 10px #e6c87a66;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .main-container {
            padding: 1rem;
        }
        
        .section-title {
            font-size: 1.5rem !important;
        }
        
        .result-card {
            padding: 1rem !important;
        }
        
        .metric-box {
            padding: 1rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def get_asb_colors():
    """Return ASB Reports color palette"""
    return {
        'purple': '#8b5cf6',
        'magenta': '#d946ef', 
        'gold': '#d4af37',
        'text': '#1e1b4b',
        'surface': '#ffffff',
        'background': '#fdf8f4',
        'gradient': 'linear-gradient(90deg, #8b5cf6, #d946ef)'
    }
