


def get_stock():
    t = yf.Ticker("APPL")
    return t.history(period="1000y")


def _check_if_symbol_exist(stock: yf.Ticker) -> bool:
    """
    Checks if this stock really exists

    Specific explanation about that code:
    We didn't use "stock.info" because it takes a few seconds and the
    output is not obvious.
    WARNING: the fast_info can change it's output someday
    :param stock: the stock object after running "yf.Ticker(<symbol>)"
    :return: None if doesn't exist, json if it does. False if nothing, True if something
    """
    return bool(stock._fast_info)


def _check_if_valid_symbol(symbol: str) -> bool:
    """
    This function runs a regex that should get all the stock Symbols possible

    :param symbol: represents the stock such as APLL (Apple), or MSFT (Microsoft)
    """
    pattern = re.compile(r'^[A-Z0-9.-]{1,5}$')
    return bool(pattern.match(symbol))
