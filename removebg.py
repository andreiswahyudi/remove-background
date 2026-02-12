import streamlit as st
from transparent_background import Remover
from PIL import Image
import io
import zipfile
import sys  
import os   

# 1. Konfigurasi Halaman (Harus di baris pertama eksekusi Streamlit)
st.set_page_config(page_title="Bakground Remove", layout="centered")

# --- CSS Injection untuk Tema Classic 90s ---
st.markdown("""
<style>
    /* Global Background & Font */
    .stApp {
        background-color: #000000;
        color: #e0e0e0;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #ffffff !important;
        border-bottom: 2px solid #ffffff;
        padding-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Buttons (Retro Style: Kotak, High Contrast) */
    .stButton>button {
        color: #000000 !important;
        background-color: #ffffff !important;
        border: 2px solid #ffffff !important;
        border-radius: 0px !important; /* Sudut Tajam */
        font-family: 'Courier New', Courier, monospace !important;
        font-weight: bold !important;
        box-shadow: 5px 5px 0px #333333;
        transition: all 0.1s;
    }
    .stButton>button:active {
        box-shadow: 2px 2px 0px #333333;
        transform: translateY(3px);
    }
    .stButton>button:hover {
        background-color: #cccccc !important;
        border-color: #cccccc !important;
    }

    /* File Uploader Area */
    [data-testid='stFileUploader'] {
        border: 2px dashed #ffffff;
        padding: 20px;
        background-color: #111111;
    }
    
    /* Progress Bar Color */
    .stProgress > div > div > div > div {
        background-color: #ffffff;
    }

    /* Download Button Specifics */
    .stDownloadButton>button {
        color: #ffffff !important;
        background-color: #000000 !important;
        border: 2px solid #ffffff !important;
    }
    .stDownloadButton>button:hover {
        background-color: #333333 !important;
    }

    /* Hide Default Streamlit Elements (Menu, Footer) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# --- Logic Backend (Tetap Sama) ---
@st.cache_resource
def get_remover():
    return Remover(mode='base') 

# --- Interface Utama ---
st.title("Background Remove")
st.markdown("V. 1.0")

uploaded_files = st.file_uploader(
    "INPUT DATA STREAM (MAX 100 FILES)", 
    type=['png', 'jpg', 'jpeg', 'webp'], 
    accept_multiple_files=True
)

if uploaded_files:
    file_count = len(uploaded_files)
    
    # Audit logic
    if file_count > 100:
        st.error(f"[ERROR] OVERLOAD: {file_count} FILES DETECTED. LIMIT: 100.")
    else:
        st.write(f"Detected: {file_count} files. Ready to process.")
        
        if st.button("PROCESS"):
            remover = get_remover()
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            zip_buffer = io.BytesIO()
            
            with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                for i, uploaded_file in enumerate(uploaded_files):
                    try:
                        status_text.code(f"PROCESSING_NODE_{i+1}: {uploaded_file.name}...")
                        
                        image = Image.open(uploaded_file).convert("RGB")
                        out = remover.process(image)
                        
                        file_name = uploaded_file.name.rsplit('.', 1)[0] + "_clean.png"
                        img_byte_arr = io.BytesIO()
                        out.save(img_byte_arr, format='PNG')
                        
                        zip_file.writestr(file_name, img_byte_arr.getvalue())
                        progress_bar.progress((i + 1) / file_count)
                        
                    except Exception as e:
                        st.warning(f"[FAIL] {uploaded_file.name}: {e}")

            status_text.code(">> OPERATION COMPLETE.")
            progress_bar.progress(100)
            
            st.download_button(
                label="[DOWNLOAD ARCHIVE.ZIP]",
                data=zip_buffer.getvalue(),
                file_name="processed_images.zip",
                mime="application/zip"
            )

st.divider()
st.code("""
// Author: Andre Xyz
""")