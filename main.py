from dotenv import load_dotenv
from stockmarket.crew import StockmarketCrew

load_dotenv()
def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'is it good to buy APPL adn TSLA this week?'
    }
    StockmarketCrew().crew().kickoff(inputs=inputs)

run()

# run dengan python -m stockmarket.main ke console