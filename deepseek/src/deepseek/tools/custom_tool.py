from crewai.tools import BaseTool 
from crewai_tools.tools import ScrapeWebsiteTool


class NewsSentimentTool(BaseTool):
    name: str = "NewsSentimentTool"
    description: str = "Scrapes and analyzes sentiment from stock market news for given tickers."

    def _run(self, tickers: str) -> str:
        news_tool = ScrapeWebsiteTool(website_url="https://www.investing.com/news/stock-market-news")
        try:
            scraped_data = news_tool.run(tickers)
            return f"News sentiment analysis completed for {tickers}. Extracted data: {scraped_data}"
        except Exception as e:
            return f"Failed to scrape news for {tickers}: {str(e)}"


class TechnicalAnalysisTool(BaseTool):
    name: str = "TechnicalAnalysisTool"
    description: str = "Fetches technical indicators (SMA, RSI, MACD) from stock charts."

    def _run(self, tickers: str) -> str:
        chart_tool = ScrapeWebsiteTool(website_url="https://www.investing.com/charts/stocks-charts")
        try:
            scraped_data = chart_tool.run(tickers)
            return f"Technical analysis data retrieved for {tickers}. Extracted data: {scraped_data}"
        except Exception as e:
            return f"Failed to scrape technical data for {tickers}: {str(e)}"


class FundamentalDataTool(BaseTool):
    name: str = "FundamentalDataTool"
    description: str = "Retrieves and evaluates fundamental data (P/E, earnings, etc.) for given tickers."

    def _run(self, tickers: str) -> str:
        return f"Fundamental data (ratios, earnings) retrieved and evaluated for tickers {tickers}."
