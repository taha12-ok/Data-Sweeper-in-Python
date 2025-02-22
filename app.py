import streamlit as st 
import pandas as pd 
import os
from io import BytesIO

# Set up page configuration
st.set_page_config(
    page_title="Data Sweeper Pro",
    layout='wide',
    initial_sidebar_state="expanded"
)

# Professional theme and styling
st.markdown("""
    <style>
    /* Main theme colors and styles */
    :root {
        --primary-color: #2E86C1;
        --secondary-color: #3498DB;
        --accent-color: #1ABC9C;
        --background-color: #F8F9FA;
        --card-background: #FFFFFF;
        --text-color: #2C3E50;
    }
    
    /* Global styles */
    .main {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2rem;
    }
    
    /* Title styling */
    .stTitle {
        color: var(--primary-color);
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        text-align: center;
        padding: 2rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Card container styling */
    .css-1d391kg {
        background-color: var(--card-background);
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    /* Subheader styling */
    .stSubheader {
        color: var(--text-color);
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        padding: 1rem 0;
        border-bottom: 2px solid var(--accent-color);
        margin-bottom: 1rem;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* File uploader styling */
    .uploadedFile {
        background-color: var(--card-background);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 2px dashed var(--primary-color);
    }
    
    /* Success message styling */
    .stSuccess {
        background: linear-gradient(45deg, #28a745, #20c997);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: 600;
    }
    
    /* Info message styling */
    .stInfo {
        background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
        color: white;
        padding: 1rem;
        border-radius: 10px;
    }
    
    /* DataFrame styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: var(--card-background);
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }
    
    /* Radio button styling */
    .stRadio > label {
        color: var(--text-color);
        font-weight: 500;
    }
    
    /* Checkbox styling */
    .stCheckbox > label {
        color: var(--text-color);
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

# App header with professional description
st.title("✨ Data Sweeper Pro")
st.markdown("""
    <div style='background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%); 
                padding: 2rem; 
                border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
                margin-bottom: 2rem;'>
        <h3 style='color: #2E86C1; margin-bottom: 1rem;'>Transform Your Data with Professional Tools</h3>
        <p style='color: #2C3E50; font-size: 1.1rem; margin-bottom: 1.5rem;'>
            A powerful data processing suite designed for professionals who demand efficiency and precision.
        </p>
        <div style='background: #F1F8FF; padding: 1rem; border-radius: 8px; border-left: 4px solid #2E86C1;'>
            <h4 style='color: #2E86C1; margin-bottom: 0.5rem;'>Key Features:</h4>
            <ul style='color: #2C3E50; margin-bottom: 0;'>
                <li>Seamless conversion between CSV and Excel formats</li>
                <li>Advanced data cleaning and preprocessing</li>
                <li>Interactive data visualization tools</li>
                <li>Bulk file processing capabilities</li>
                <li>Professional-grade error handling</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

# File upload section with styled container
uploaded_files = st.file_uploader(
    "Upload your files (CSV or Excel):", 
    type=["csv", "xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        st.markdown(f"""
            <div style='background: white; 
                        padding: 2rem; 
                        border-radius: 15px; 
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
                        margin: 2rem 0;'>
                <h3 style='color: #2E86C1;'>📄 Processing: {file.name}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Read the file
        file_ext = os.path.splitext(file.name)[1].lower()
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue
                
            # File information in styled columns
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                    <div style='background: linear-gradient(135deg, #E1F5FE 0%, #B3E5FC 100%);
                              padding: 1rem;
                              border-radius: 10px;
                              text-align: center;'>
                        <h4 style='color: #0277BD; margin: 0;'>📊 Data Dimensions</h4>
                        <p style='color: #01579B; font-size: 1.2rem; margin: 0;'>
                            Rows: {df.shape[0]} | Columns: {df.shape[1]}
                        </p>
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                    <div style='background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
                              padding: 1rem;
                              border-radius: 10px;
                              text-align: center;'>
                        <h4 style='color: #2E7D32; margin: 0;'>💾 File Size</h4>
                        <p style='color: #1B5E20; font-size: 1.2rem; margin: 0;'>
                            {file.size/1024:.2f} KB
                        </p>
                    </div>
                """, unsafe_allow_html=True)

            # Data preview in expandable section
            with st.expander("🔍 Preview Data", expanded=False):
                st.dataframe(df.head(), use_container_width=True)

            # Data cleaning options
            st.subheader("🧹 Data Cleaning Options")
            clean_col1, clean_col2 = st.columns(2)

            with clean_col1:
                if st.button("🔄 Remove Duplicates", key=f"dup_{file.name}"):
                    initial_rows = len(df)
                    df.drop_duplicates(inplace=True)
                    st.success(f"Removed {initial_rows - len(df)} duplicate rows!")

            with clean_col2:
                if st.button("📝 Fill Missing Values", key=f"fill_{file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("Missing values have been filled!")

            # Column selection with styled container
            st.subheader("📋 Column Selection")
            columns = st.multiselect(
                "Choose columns to keep:",
                df.columns,
                default=df.columns,
                key=f"cols_{file.name}"
            )
            df = df[columns]

            # Visualizations
            st.subheader("📊 Data Visualization")
            if st.checkbox("Show visualizations", key=f"viz_{file.name}"):
                numeric_df = df.select_dtypes(include='number')
                if not numeric_df.empty:
                    st.bar_chart(numeric_df.iloc[:,:2], use_container_width=True)
                else:
                    st.warning("No numeric columns available for visualization")

            # File conversion with styled container
            st.subheader("💾 Convert and Download")
            conversion_type = st.radio(
                "Convert to:",
                ["CSV", "Excel"],
                key=f"conv_{file.name}"
            )
            
            if st.button("Convert and Download", key=f"download_{file.name}"):
                try:
                    buffer = BytesIO()
                    new_filename = os.path.splitext(file.name)[0]
                    
                    if conversion_type == "CSV":
                        df.to_csv(buffer, index=False)
                        mime_type = "text/csv"
                        final_filename = f"{new_filename}.csv"
                    else:  # Excel
                        df.to_excel(buffer, index=False)
                        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        final_filename = f"{new_filename}.xlsx"
                    
                    buffer.seek(0)
                    st.download_button(
                        label=f"📥 Download as {conversion_type}",
                        data=buffer,
                        file_name=final_filename,
                        mime=mime_type
                    )
                except Exception as e:
                    st.error(f"Error during conversion: {str(e)}")
                    
        except Exception as e:
            st.error(f"Error processing {file.name}: {str(e)}")

    st.markdown("""
        <div style='background: linear-gradient(135deg, #D4EDDA 0%, #C3E6CB 100%);
                    padding: 1.5rem;
                    border-radius: 10px;
                    text-align: center;
                    margin-top: 2rem;'>
            <h3 style='color: #155724; margin: 0;'>🎉 All files processed successfully!</h3>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #CFF4FC 0%, #B6EFFB 100%);
                    padding: 1.5rem;
                    border-radius: 10px;
                    text-align: center;
                    margin-top: 2rem;'>
            <h3 style='color: #055160; margin: 0;'>👆 Upload your files to get started!</h3>
        </div>
    """, unsafe_allow_html=True)