import pandas


def calculate_moving_average(data: pandas.core.frame.DataFrame, window: int=7) -> pandas.core.series.Series:
    """

    :param data:
    :param window:
    :return:
    """
    # TODO: what is the meaning?
    return data["Close"].rolling(window=window).mean()

def calculate_momentum(data: pandas.core.frame.DataFrame, shift: int=4) -> pandas.core.series.Series:
    """

    :param data:
    :param shift:
    :return:
    """
    # TODO why shift 4?
    return data['Close'] - data['Close'].shift(shift)
