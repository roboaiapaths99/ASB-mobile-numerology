import streamlit as st
import pandas as pd
from datetime import datetime
import time

from mobile_numerology.consultation import NumerologyConsultation
from asb_theme import apply_asb_theme, get_asb_colors

# Page configuration
st.set_page_config(
    page_title="Mobile Numerology Consultation", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply ASB Reports inspired theme
apply_asb_theme()

    .header-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at top right, rgba(255,255,255,0.1) 0%, transparent 60%);
    }

    .header-section h1 {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-family: 'Cinzel', serif;
        letter-spacing: 3px;
    }

    .header-section p {
        font-size: 1.2rem;
        opacity: 0.95;
        margin-top: 12px;
        font-weight: 500;
        letter-spacing: 1px;
    }

    .input-card {
        background: linear-gradient(145deg, #ffffff 0%, #faf7f2 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border: 1.5px solid #e8d4a0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 3px 12px rgba(212, 175, 55, 0.1);
    }

    .input-card:hover {
        border-color: #d4af37;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.25);
        transform: translateY(-2px);
    }

    .section-title {
        background: linear-gradient(135deg, #d4af37 0%, #b8941f 50%, #8b6914 100%);
        color: white;
        padding: 16px 28px;
        border-radius: 12px;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 30px 0 20px 0;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.3);
        font-family: 'Cinzel', serif;
        letter-spacing: 1.5px;
    }

    .metric-box {
        background: linear-gradient(145deg, #ffffff 0%, #faf7f2 100%);
        color: #2c1810;
        padding: 22px;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 5px 18px rgba(212, 175, 55, 0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1.5px solid #e8d4a0;
    }

    .metric-box:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.35);
        border-color: #d4af37;
    }

    .metric-box.blue {
        background: linear-gradient(145deg, #fffbf0 0%, #fff5e1 100%);
        border-color: #d4af37;
        color: #8b6914;
    }

    .metric-box.green {
        background: linear-gradient(145deg, #f0fff4 0%, #e6f7ed 100%);
        border-color: #a8d4b3;
        color: #2d5a3d;
    }

    .metric-box.orange {
        background: linear-gradient(145deg, #fff5f0 0%, #ffe8e0 100%);
        border-color: #d4a088;
        color: #8b4513;
    }
    
    .metric-box h3 {
        font-size: 2.5rem;
        margin: 0;
        font-weight: 700;
    }
    
    .metric-box p {
        margin: 5px 0 0 0;
        opacity: 0.9;
        font-size: 0.9rem;
    }
    
    .grid-container {
        background: linear-gradient(135deg, #faf7f2 0%, #f5ebe0 50%, #fae5d8 100%);
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #d4af37;
        margin: 20px auto;
        max-width: 500px;
        box-shadow: 0 10px 40px rgba(212, 175, 55, 0.15);
    }
    
    .grid-title {
        text-align: center;
        font-size: 1.4rem;
        font-weight: 600;
        color: #8b6914;
        margin-bottom: 25px;
        font-family: 'Cinzel', serif;
        letter-spacing: 2px;
    }
    
    .lo-shu-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin-bottom: 20px;
    }
    
    .grid-cell {
        aspect-ratio: 1;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.8rem;
        font-weight: 600;
        color: #2c1810;
        background: linear-gradient(145deg, #ffffff 0%, #faf7f2 100%);
        border: 1.5px solid #d4af37;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-family: 'Cinzel', serif;
        position: relative;
        overflow: hidden;
    }
    
    .grid-cell::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at center, rgba(212, 175, 55, 0.1) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .grid-cell:hover {
        transform: scale(1.08);
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.35);
        border-color: #b8941f;
    }
    
    .grid-cell:hover::before {
        opacity: 1;
    }
    
    .grid-cell.missing {
        background: linear-gradient(145deg, #fff5f5 0%, #ffe8e8 100%);
        border-color: #c9a87c;
        color: #8b4513;
    }
    
    .grid-cell.missing:hover {
        box-shadow: 0 8px 25px rgba(139, 69, 19, 0.25);
        border-color: #a0785a;
    }
    
    .grid-cell.present {
        background: linear-gradient(145deg, #ffffff 0%, #faf7f2 100%);
        border-color: #d4af37;
        color: #2c1810;
    }
    
    .grid-cell.multiple {
        background: linear-gradient(145deg, #fffbf0 0%, #fff5e1 100%);
        border-color: #d4af37;
        color: #8b6914;
        flex-direction: column;
        font-size: 2.2rem;
    }
    
    .grid-cell .count {
        font-size: 0.75rem;
        margin-top: 4px;
        opacity: 0.85;
        font-weight: 500;
        font-family: 'Poppins', sans-serif;
        letter-spacing: 0.5px;
    }
    
    .result-card {
        background: linear-gradient(145deg, #ffffff 0%, #faf7f2 100%);
        border-left: 5px solid #d4af37;
        padding: 20px;
        margin: 15px 0;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.15);
        transition: all 0.3s ease;
    }

    .result-card:hover {
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.25);
        transform: translateX(3px);
    }

    .result-card h4 {
        color: #8b6914;
        margin: 0 0 10px 0;
        font-size: 1.1rem;
        font-family: 'Cinzel', serif;
        letter-spacing: 0.5px;
    }

    .result-card p {
        margin: 0;
        color: #5a4a3a;
        line-height: 1.6;
    }

    .success-banner {
        background: linear-gradient(135deg, #d4af37 0%, #b8941f 50%, #8b6914 100%);
        color: white;
        padding: 22px;
        border-radius: 14px;
        text-align: center;
        margin: 25px 0;
        font-size: 1.5rem;
        font-weight: 600;
        box-shadow: 0 8px 30px rgba(212, 175, 55, 0.35);
        font-family: 'Cinzel', serif;
        letter-spacing: 1.5px;
    }

    .error-banner {
        background: linear-gradient(135deg, #d4a088 0%, #c4856a 100%);
        color: white;
        padding: 16px;
        border-radius: 12px;
        text-align: center;
        margin: 12px 0;
        font-weight: 500;
    }

    .stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #b8941f 50%, #8b6914 100%);
        color: white;
        border: none;
        padding: 16px 32px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 5px 18px rgba(212, 175, 55, 0.3);
        font-family: 'Cinzel', serif;
        letter-spacing: 1px;
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.45);
    }
    
    .legend {
        text-align: center;
        padding: 18px;
        background: linear-gradient(135deg, #ffffff 0%, #faf7f2 100%);
        border-radius: 12px;
        margin-top: 20px;
        border: 1px solid #e8d4a0;
        font-family: 'Poppins', sans-serif;
    }
    
    .legend-item {
        display: inline-block;
        margin: 0 20px;
        font-size: 0.9rem;
        color: #5a4a3a;
        font-weight: 500;
    }
    
    .legend-dot {
        display: inline-block;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        margin-right: 6px;
        border: 1.5px solid rgba(212, 175, 55, 0.3);
    }
    
    .legend-dot.blue { 
        background: linear-gradient(145deg, #ffffff 0%, #faf7f2 100%);
        border-color: #d4af37;
    }
    .legend-dot.green { 
        background: linear-gradient(145deg, #fffbf0 0%, #fff5e1 100%);
        border-color: #d4af37;
    }
    .legend-dot.red { 
        background: linear-gradient(145deg, #fff5f5 0%, #ffe8e8 100%);
        border-color: #c9a87c;
    }
</style>
""", unsafe_allow_html=True)

# Main Container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-section">
    <h1>✨ Sacred Numerology</h1>
    <p>Discover Your Divine Numerological Blueprint</p>
</div>
""", unsafe_allow_html=True)

# Input Section
st.markdown('<div class="section-title">✨ Enter Your Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    name = st.text_input("👤 Client Name", placeholder="Enter your full name", label_visibility="visible")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    dob = st.date_input("📅 Date of Birth", value=datetime(1996, 5, 27))
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    mobile_number = st.text_input("📱 Mobile Number", placeholder="Enter 10-digit number", help="Enter 10-digit mobile number")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    challenges = st.text_area("🎯 Current Life Challenges", placeholder="Career, Health, Relationships...", height=80)
    st.markdown('</div>', unsafe_allow_html=True)

# Generate Button
if st.button("✨ Generate Sacred Report", type="primary"):
    if not name or not mobile_number:
        st.markdown('<div class="error-banner">⚠️ Please fill in Name and Mobile Number</div>', unsafe_allow_html=True)
    elif len(mobile_number) != 10 or not mobile_number.isdigit():
        st.markdown('<div class="error-banner">⚠️ Please enter a valid 10-digit mobile number</div>', unsafe_allow_html=True)
    else:
        # Progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Convert date to string format
            dob_str = dob.strftime("%d/%m/%Y")
            consultation = NumerologyConsultation(name, dob_str, mobile_number, challenges)
            
            status_text.text("🔢 Calculating numerology grids...")
            progress_bar.progress(25)
            time.sleep(0.3)
            
            name_dob_grid = consultation.generate_name_dob_grid()
            
            status_text.text("📊 Analyzing patterns...")
            progress_bar.progress(50)
            time.sleep(0.3)
            
            results = consultation.generate_consultation_report()
            
            status_text.text("💎 Preparing insights...")
            progress_bar.progress(75)
            time.sleep(0.3)
            
            progress_bar.progress(100)
            status_text.text("✅ Report generated successfully!")
            time.sleep(0.5)
            progress_bar.empty()
            status_text.empty()
            
            # Success Banner
            st.markdown('<div class="success-banner">✨ Your Sacred Report is Ready ✨</div>', unsafe_allow_html=True)

            # Personal Information
            st.markdown('<div class="section-title">✨ Personal Information</div>', unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="metric-box blue">
                    <h3>{name}</h3>
                    <p>Client Name</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-box green">
                    <h3>{dob.strftime('%d-%m-%Y')}</h3>
                    <p>Date of Birth</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="metric-box orange">
                    <h3>{mobile_number}</h3>
                    <p>Mobile Number</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Core Numbers
            st.markdown('<div class="section-title">✨ Core Numbers</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                <div class="metric-box blue">
                    <h3>{results['moolank']}</h3>
                    <p>Moolank (Birth Day)</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-box green">
                    <h3>{results['bhagyank']}</h3>
                    <p>Bhagyank (Destiny)</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Lo Shu Grid completely removed from frontend

            # Number Classification

            # Number Classification
            st.markdown('<div class="section-title">✨ Number Classification</div>', unsafe_allow_html=True)

            classification = results['classification']

            col1, col2, col3 = st.columns(3)

            with col1:
                friendly = ', '.join(map(str, classification['friendly'])) if classification['friendly'] else "None"
                st.markdown(f"""
                <div class="result-card">
                    <h4>✅ Friendly Numbers</h4>
                    <p>{friendly}</p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                enemy = ', '.join(map(str, classification['enemy'])) if classification['enemy'] else "None"
                st.markdown(f"""
                <div class="result-card">
                    <h4>❌ Enemy Numbers</h4>
                    <p>{enemy}</p>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                neutral = ', '.join(map(str, classification['neutral'])) if classification['neutral'] else "None"
                st.markdown(f"""
                <div class="result-card">
                    <h4>⚖️ Neutral Numbers</h4>
                    <p>{neutral}</p>
                </div>
                """, unsafe_allow_html=True)

            # Pair Analysis
            st.markdown('<div class="section-title">✨ Pair Analysis</div>', unsafe_allow_html=True)
            
            pair_df = pd.DataFrame(results['pair_analysis'])
            if not pair_df.empty:
                # Style the dataframe to highlight good and bad pairs
                def highlight_pairs(row):
                    if row['type'] == 'Good':
                        return ['background-color: #e6f7ed; color: #2d5a3d; font-weight: 600'] * len(row)
                    elif row['type'] == 'Bad':
                        return ['background-color: #ffe8e0; color: #8b4513; font-weight: 600'] * len(row)
                    else:
                        return [''] * len(row)

                styled_df = pair_df[['serial', 'pair', 'type']].style.apply(highlight_pairs, axis=1)
                st.dataframe(styled_df, use_container_width=True, hide_index=True)
            
            # Final Result
            st.markdown('<div class="section-title">✨ Final Result</div>', unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="result-card">
                <h4>{results['final_result']}</h4>
                <p>{results['interpretation']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Remedies
            st.markdown('<div class="section-title">✨ Remedies & Recommendations</div>', unsafe_allow_html=True)
            
            remedies = results['remedies']
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                directions = ', '.join(remedies['directions'])
                st.markdown(f"""
                <div class="result-card">
                    <h4>🧭 Charging Direction</h4>
                    <p>{directions}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                color_info = remedies['color_info']
                st.markdown(f"""
                <div class="result-card">
                    <h4>🎨 Lucky Color</h4>
                    <p>{color_info['color']}</p>
                    <p><small>Planet: {color_info['planet']}</small></p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                crystals = ', '.join(remedies['crystals']) if remedies['crystals'] else "None needed"
                st.markdown(f"""
                <div class="result-card">
                    <h4>💎 Recommended Crystals</h4>
                    <p>{crystals}</p>
                    <p><small><a href="https://asbcrystal.in/" target="_blank">🔮 Buy Crystals Online</a></small></p>
                </div>
                """, unsafe_allow_html=True)
            
        except Exception as e:
            st.markdown(f'<div class="error-banner">❌ Error generating report: {str(e)}</div>', unsafe_allow_html=True)
            st.markdown('<div class="error-banner">Please check that all inputs are valid and try again.</div>', unsafe_allow_html=True)

# Close main container
st.markdown('</div>', unsafe_allow_html=True)
