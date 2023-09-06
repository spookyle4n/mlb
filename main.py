import requests
import json
import time

# Define the API endpoint for the live MLB database
mlb_api_endpoint = "https://api.mlbdata.com/live/yankees"

try:
    while True:
        # Make a request to the API endpoint
        response = requests.get(mlb_api_endpoint)

        # Check for a successful response
        if response.status_code == 200:
            # Parse the JSON data for the Yankees game
            yankees_game_data = json.loads(response.text)

            # Extract relevant information from the data
            game_score = yankees_game_data['score']
            inning = yankees_game_data['inning']
            pitcher = yankees_game_data['pitcher']
            batter = yankees_game_data['batter']
            balls = yankees_game_data['balls']
            strikes = yankees_game_data['strikes']
            # Add more data as needed

            # Display the live information
            print(f"Yankees Game Score: {game_score}")
            print(f"Current Inning: {inning}")
            print(f"Yankees Pitcher: {pitcher}")
            print(f"Yankees Batter: {batter}")
            print(f"Balls: {balls}")
            print(f"Strikes: {strikes}")
            # Display more game details as necessary

        else:
            print("Error: Unable to retrieve data from the MLB database.")

        # Wait for a moment before updating the information again (adjust the delay as needed)
        time.sleep(60)  # Update every minute

except KeyboardInterrupt:
    print("Script terminated by user.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
