"""
Script 1: football_stats.py
Scrapes NFL passing statistics from CBS Sports.
URL: https://www.cbssports.com/nfl/stats/player/passing/nfl/regular
"""

from bs4 import BeautifulSoup
import urllib.request

def scrape_football_stats():
    url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular"
    
    # Add User-Agent header to prevent 403 Forbidden blocks
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    
    try:
        html = urllib.request.urlopen(req).read()
    except Exception as e:
        print(f"Error accessing URL: {e}")
        return

    soup = BeautifulSoup(html, 'lxml')
    
    # Locate the stats table
    table = soup.find('table')
    if not table:
        print("Could not find stats table.")
        return
        
    rows = table.find_all('tr')
    
    print("=== Top NFL Passing Stats ===")
    count = 0
    for row in rows[1:]:
        text = row.get_text(separator=" | ", strip=True)
        if text:
            print(text)
            count += 1
            if count >= 20:  # Top 20 players
                break

if __name__ == "__main__":
    scrape_football_stats()
