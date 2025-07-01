# scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_linkedin_profile(profile_url: str) -> dict:
    """
    Initiates an HTTP GET request to a public LinkedIn profile and parses the HTML response.

    Args:
        profile_url: The full URL of the public LinkedIn profile to be scraped.

    Returns:
        A dictionary containing the extracted professional data.
        Returns a dictionary with an 'error' key if an exception occurs.
    """
    try:
        # A valid User-Agent is crucial to mimic a legitimate browser request.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(profile_url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.text, 'html.parser')

        # --- Data Extraction ---
        # NOTE: These CSS selectors are illustrative examples. They must be updated
        # by inspecting the current HTML structure of a live LinkedIn profile.
        
        # Example: Extracting the name
        name_element = soup.find('h1', {'class': 'top-card-layout__title'})
        name = name_element.get_text(strip=True) if name_element else "Not Found"

        # Example: Extracting the headline/title
        headline_element = soup.find('h2', {'class': 'top-card-layout__headline'})
        headline = headline_element.get_text(strip=True) if headline_element else "Not Found"
        
        # Example: Extracting the location
        location_element = soup.find('span', {'class': 'top-card__subline-item'})
        location = location_element.get_text(strip=True) if location_element else "Not Found"

        profile_data = {
            'Name': name,
            'Headline': headline,
            'Location': location,
        }
        
        return profile_data

    except requests.exceptions.RequestException as e:
        return {'error': f"HTTP Request failed: {e}"}
    except Exception as e:
        return {'error': f"An unexpected error occurred: {e}"}

