import pandas as pd
import logging as log

from datetime import datetime as dt
from yahoo_fin import options as yo

import core.constants as c

log.basicConfig(format='%(levelname)s:%(message)s', level=log.INFO)


def get_all_calls(ticker: str) -> pd.DataFrame:
    dates = yo.get_expiration_dates(ticker)
    dates = [dt.strptime(da, c.YAHOO_DATE_FMT) for da in dates]
    log.info(f'Calls found for {ticker} with dates: {dates}')
    calls_df = pd.concat(
        {da: yo.get_calls(ticker=ticker, date=da).set_index('Contract Name') for da in dates},
        0,
        names=['Date', 'Contract Name']
    )

    return calls_df
