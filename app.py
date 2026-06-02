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
with st.container():
    col1, col2 = st.columns([1, 1])
    
    with col1:
        name = st.text_input("👤 Full Name", placeholder="Enter your full name")
        dob = st.date_input("📅 Date of Birth", value=datetime(1996, 5, 27))
    
    with col2:
        mobile = st.text_input("📱 Mobile Number", placeholder="Enter your 10-digit mobile number")
        challenges = st.text_area("🎯 Current Challenges", placeholder="Describe your current life challenges")

# Consultation Button
if st.button("🔮 Generate Numerology Consultation", type="primary"):
    if name and dob and mobile:
        try:
            # Format date
            dob_str = dob.strftime("%d/%m/%Y")
            
            # Create consultation
            consultation = NumerologyConsultation(name, dob_str, mobile, challenges)
            
            # Generate report
            results = consultation.generate_consultation_report()
            
            # Display results
            st.markdown("---")
            
            # Personal Information
            st.markdown('<div class="section-title">✨ Personal Information</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class="result-card">
                    <h4>👤 Name</h4>
                    <p>{results['client_info']['name']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="result-card">
                    <h4>📅 Date of Birth</h4>
                    <p>{results['client_info']['dob']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="result-card">
                    <h4>📱 Mobile Number</h4>
                    <p>{results['client_info']['mobile']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if results['client_info']['challenges']:
                    st.markdown(f"""
                    <div class="result-card">
                        <h4>🎯 Current Challenges</h4>
                        <p>{results['client_info']['challenges']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Core Numbers
            st.markdown('<div class="section-title">✨ Core Numbers</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class="metric-box gold">
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
