import pandas
import yfinance as yf

from lab import calculate_moving_average
from utils import _check_if_valid_symbol, _check_if_symbol_exist


class Stock():
    def __init__(self, symbol, period):
        self.symbol = symbol
        self.period = period
        self.ticker = self.get_stock_object(self.symbol)

    def get_stock_history_data_frame(self) -> pandas.core.farame.DataFrame:
        """
        This function gets all the historical stock data
        TODO: check if we can optimize results by looking at different scope
        :return: DataFrame with all the historical data
        """
        return self.ticker.history("max")

    def get_stock_object(self, symbol):
        """

        :param symbol:
        :return:
        """
        if not symbol.isascii():
            raise Exception(f"Bad format {str(symbol)}, not ascii")
        if _check_if_valid_symbol(symbol):
            ticker = yf.Ticker(symbol)
            if not _check_if_symbol_exist(ticker):
                raise Exception(f"Symbol {str(symbol)} doesn't found")
            return ticker

    def get_prepared_stock(self, data: pandas.core.frame.DataFrame) -> int:
        """
        This function runs all the key elements before creating the ML's.
        - It cleans the data
        - It removes uneccesry columns TODO add that logic
        - It adds several important columns
        :return:
        """
        data.sort_values(by='date', inplace=True)
        data["IsUp"] = (data['Close'].shift(-1) > data['Close']).astype(int)
        data = data[:-1]  # Dropping the last row because no IsUp possible TODO check that

        # TODO remove columns

        # Adding specific columns
        data["MA"] = calculate_moving_average(data, 7)
        data["Momentum"] =