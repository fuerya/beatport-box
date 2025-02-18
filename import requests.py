from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options (remove "--headless" if you want to see the browser)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Remove this line if you want to see the browser
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set up Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Beatport
url = "https://www.beatport.com"
driver.get(url)

# Wait for the page to load
time.sleep(5)

# WebDriver wait object
wait = WebDriverWait(driver, 15)

# Track last song to prevent duplicate prints
last_song = None

while True:
    try:
        # Locate the player container (ensures we get the **currently playing** track)
        player_container = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Player')]"))
        )

        # Extract track name from currently playing track
        track_name = player_container.find_element(By.XPATH, ".//span[contains(@class, 'Player-style__TrackName')]").text

        # Extract mix name from currently playing track
        mix_name = player_container.find_element(By.XPATH, ".//span[contains(@class, 'Player-style__MixName')]").text

        # Combine track details
        current_song = f"{track_name} - {mix_name}"

        # Print only if the song has changed
        if current_song != last_song:
            print(current_song)
            last_song = current_song
