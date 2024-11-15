from rufus_client import RufusClient
import os

# Optional: Set API Key (not functionally required)
os.environ["Rufus_API_KEY"] = "your_api_key_here"

# Initialize RufusClient
client = RufusClient(api_key=os.getenv("Rufus_API_KEY"))

# Define the URL and depth
url = "https://www.sfgov.org"
depth = 2

# Perform the scrape
documents = client.scrape(url, depth=depth)

# Save output to JSON
client.save_to_json(documents, "structured_output-2.json")

# Close the client
client.close()
