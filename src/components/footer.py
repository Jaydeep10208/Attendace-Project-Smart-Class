import streamlit as st
from datetime import datetime

def footer_home():
    current_year = datetime.now().year
    st.markdown(f"""
        <style>
            @keyframes gradient-shift {{
                0% {{ background-position: 0% 50%; }}
                50% {{ background-position: 100% 50%; }}
                100% {{ background-position: 0% 50%; }}
            }}
            
            @keyframes float {{
                0%, 100% {{ transform: translateY(0px); }}
                50% {{ transform: translateY(-12px); }}
            }}
            
            .footer-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                width: 100%;
                margin: 4rem 0 0 0;
                padding: 4rem 2rem;
                background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
                background-size: 400% 400%;
                animation: gradient-shift 15s ease infinite;
                border-radius: 20px;
                box-shadow: 0 -20px 60px rgba(0, 0, 0, 0.3),
                            inset 0 1px 0 rgba(255, 255, 255, 0.1),
                            0 0 100px rgba(102, 126, 234, 0.2);
                position: relative;
                overflow: hidden;
                border: none;
                box-sizing: border-box;
            }}
            
            .footer-container::before {{
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: radial-gradient(circle, rgba(102, 126, 234, 0.08) 1px, transparent 1px);
                background-size: 50px 50px;
                animation: float 20s linear infinite;
                pointer-events: none;
                opacity: 0.5;
            }}
            
            .footer-container::after {{
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: 
                    radial-gradient(circle at 20% 50%, rgba(102, 126, 234, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 80%, rgba(240, 147, 251, 0.05) 0%, transparent 50%);
                pointer-events: none;
            }}
            
            .footer-content {{
                text-align: center;
                position: relative;
                z-index: 2;
                width: 100%;
                max-width: 900px;
            }}
            
            .footer-icon {{
                font-size: 80px;
                margin-bottom: 1.5rem;
                animation: float 4s ease-in-out infinite;
                display: inline-block;
                filter: drop-shadow(0 8px 20px rgba(102, 126, 234, 0.4));
            }}
            
            .footer-title {{
                font-size: 52px;
                font-weight: 800;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin-bottom: 1rem;
                letter-spacing: 2px;
                text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
                line-height: 1.1;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            
            .footer-divider {{
                width: 120px;
                height: 3px;
                background: linear-gradient(90deg, transparent, #667eea, #764ba2, #f093fb, transparent);
                margin: 1.2rem auto;
                border-radius: 2px;
                box-shadow: 0 0 30px rgba(102, 126, 234, 0.5),
                            0 0 60px rgba(240, 147, 251, 0.3);
            }}
            
            .footer-author {{
                font-size: 24px;
                color: rgba(255, 255, 255, 0.95);
                margin-bottom: 0.8rem;
                font-weight: 700;
                letter-spacing: 0.8px;
                text-shadow: 0 2px 10px rgba(102, 126, 234, 0.2);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            
            .footer-subtitle {{
                font-size: 16px;
                color: rgba(255, 255, 255, 0.85);
                margin-bottom: 1.5rem;
                font-weight: 500;
                letter-spacing: 0.5px;
                opacity: 0.9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            
            .footer-year {{
                font-size: 13px;
                color: rgba(255, 255, 255, 0.7);
                margin-top: 1.2rem;
                font-weight: 500;
                letter-spacing: 0.3px;
            }}
            
            .footer-badge {{
                display: inline-block;
                padding: 0.8rem 2rem;
                background: rgba(102, 126, 234, 0.15);
                border: 1.5px solid rgba(102, 126, 234, 0.5);
                border-radius: 50px;
                color: rgba(255, 255, 255, 0.95);
                font-size: 14px;
                margin-top: 1.2rem;
                backdrop-filter: blur(15px);
                font-weight: 700;
                box-shadow: 0 8px 32px rgba(102, 126, 234, 0.2),
                            inset 0 1px 1px rgba(255, 255, 255, 0.2);
                letter-spacing: 0.5px;
                transition: all 0.3s ease;
                cursor: pointer;
            }}
            
            .footer-badge:hover {{
                background: rgba(102, 126, 234, 0.25);
                box-shadow: 0 12px 40px rgba(102, 126, 234, 0.3),
                            inset 0 1px 1px rgba(255, 255, 255, 0.3);
                transform: translateY(-2px);
            }}
        </style>
        
        <div class="footer-container">
            <div class="footer-content">
                <div class="footer-icon">🎓</div>
                <div class="footer-title">Smart Class</div>
                <div class="footer-divider"></div>
                <div class="footer-author">✨ Created by JAYDEEP MISHRA ✨</div>
                <div class="footer-subtitle">Empowering Education Through Technology</div>
                <div class="footer-badge">🚀 Built with Streamlit</div>
                <div class="footer-year">© {current_year} Smart Class. All Rights Reserved.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)