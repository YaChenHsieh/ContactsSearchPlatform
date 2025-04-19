from playwright.sync_api import sync_playwright
from src.contacts.service import LinkedInSearchQueryBuilder # src.service bc from main.py later exec code
import urllib.parse
from playwright_stealth import stealth_sync

class LinkedInGoogleScraper:
    def __init__(self, headless=True):
        self.headless = headless

    def extract_names_from_google(self, query, limit=5):

        encoded_query = urllib.parse.quote_plus(query) # encode it to valid URL (eg. ("PM" OR "project manager") or "google")
        search_url = f"https://www.google.com/search?q={encoded_query}&num={limit}" 

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless) # True to run in the background
            page = browser.new_page()
            stealth_sync(page) 
            page.goto(search_url)

            page.wait_for_selector("h3", timeout=8000)

            print(f"🔎 Querying：{query}")
            print(f"🔎 URL：{search_url}")
            results = []

            # find all the h3 block (dynamic web in google class)
            h3_elements = page.query_selector_all("h3")
            print(f"✅ Found {len(h3_elements)} h3 results")

            for h3 in h3_elements:

                try:
                    title = h3.inner_text().strip() # get the text of this h3 label and strip the word
                    
                    # find the closest "a" parent() from curr h3，-> then find the link in <a>
                    parent = h3.evaluate_handle("node => node.closest('a')")
                    if parent:
                        href = parent.get_property("href").json_value()
                    else:
                        # if can NOT find a，then find the prevois a of h3
                        href = h3.evaluate("node => node.parentElement?.href || ''")

                    if "linkedin.com/in" in href or "linkedin.com/pub" in href:
                        results.append({
                            "title": title,
                            "url": href
                        })
                except Exception as e:
                    print(f"Error:{e}")
                    continue

            browser.close()
            return results


# Usage
if __name__ == "__main__":
    query = 'site:linkedin.com/in OR site:linkedin.com/pub "google" "software engineer" ("product manager" OR "project manager") "new york"'
    scraper = LinkedInGoogleScraper(headless=True)
    results = scraper.extract_names_from_google(query, limit=10)

    for r in results:
        print("👤", r["title"])
        print("🔗", r["url"])
        print()
