import streamlit as st
import pandas as pd
from scraper import scrape_linkedin_profile

st.set_page_config(page_title="LinkedIn Profile Scraper", layout="wide")

st.title("LinkedIn Profile Scraper")
st.markdown("""
**Disclaimer:** This tool is for educational purposes only. Scraping LinkedIn is against their Terms of Service.
""")

# --- User Input ---
linkedin_url = st.text_input("Enter a public LinkedIn Profile URL:")

if st.button("Scrape Profile"):
    if linkedin_url:
        with st.spinner("Scraping in progress..."):
            scraped_data = scrape_linkedin_profile(linkedin_url)

        if "error" in scraped_data:
            st.error(f"An error occurred: {scraped_data['error']}")
        else:
            st.success("Scraping successful!")
            st.subheader("Scraped Data")

            # Display the data
            df = pd.DataFrame([scraped_data])
            st.dataframe(df)

            # --- Optional: Download Button ---
            @st.cache_data
            def convert_df_to_csv(df):
                return df.to_csv(index=False).encode('utf-8')

            csv = convert_df_to_csv(df)

            st.download_button(
               label="Download data as CSV",
               data=csv,
               file_name='linkedin_profile.csv',
               mime='text/csv',
            )
    else:
        st.warning("Please enter a LinkedIn URL.")
