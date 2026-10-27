"""
Script 2: super_bowl.py
Scrapes Super Bowl champions table from Wikipedia.
URL: https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions
"""

from bs4 import BeautifulSoup
import urllib.request

def scrape_super_bowl():
    url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
    
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    try:
        html = urllib.request.urlopen(req).read()
    except Exception as e:
        print(f"Error accessing URL: {e}")
        return

    soup = BeautifulSoup(html, 'lxml')
    
    # Find the main wikitable containing Super Bowl results
    table = soup.find('table', {'class': 'wikitable'})
    if not table:
        print("Could not find Super Bowl table.")
        return
        
    rows = table.find_all('tr')
    
    print(f"{'Game':<6} | {'Date':<12} | {'Winning Team':<25} | {'Score':<8} | {'Losing Team':<25}")
    print("-" * 85)
    
    for row in rows[1:]:
        cols = row.find_all(['th', 'td'])
        if len(cols) >= 5:
            game = cols[0].get_text(strip=True)
            date = cols[1].get_text(strip=True)
            winner = cols[2].get_text(strip=True)
            score = cols[3].get_text(strip=True)
            loser = cols[4].get_text(strip=True)
            print(f"{game:<6} | {date:<12} | {winner:<25} | {score:<8} | {loser:<25}")

if __name__ == "__main__":
    scrape_super_bowl()
