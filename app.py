# app.py

import streamlit as st
import pandas as pd
from scraper import scrape_linkedin_profile

st.set_page_config(page_title="LinkedIn Data Extractor", layout="centered")

st.title("Professional Profile Data Extractor")

st.warning(
    "**Disclaimer:** This tool is for educational purposes only. "
    "Automated data collection is against LinkedIn's User Agreement."
)

# User input field for the LinkedIn profile URL
linkedin_url = st.text_input(
    "Enter a public LinkedIn Profile URL",
    placeholder="https://www.linkedin.com/in/..."
)

if st.button("Extract Data"):
    if linkedin_url:
        # Display a spinner while the backend function executes
        with st.spinner("Processing... Extracting data from the provided URL."):
            scraped_data = scrape_linkedin_profile(linkedin_url)

        if "error" in scraped_data:
            st.error(f"Failed to scrape profile: {scraped_data['error']}")
        else:
            st.success("Data extracted successfully.")
            st.subheader("Extracted Information")

            # Present the data in a clean format
            df = pd.DataFrame([scraped_data])
            st.dataframe(df, use_container_width=True)

            # Provide a download option for the data as a CSV file
            @st.cache_data
            def convert_df_to_csv(df_to_convert):
                return df_to_convert.to_csv(index=False).encode('utf-8')

            csv_data = convert_df_to_csv(df)
            st.download_button(
               label="Download data as CSV",
               data=csv_data,
               file_name='linkedin_profile_data.csv',
               mime='text/csv',
            )
    else:
        st.info("Please provide a LinkedIn profile URL to proceed.")

