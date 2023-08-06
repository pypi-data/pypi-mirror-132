<!-- [JIRNAL](https://jirnal.ir/) -->

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)

---

## Overview

It is a client-side package of Jirnal's trading system as a Binance REST Api-based SDK midleware. Valid Binance account and Jirnal account are required to work with this package.

## Requirements
- [python](https://www.python.org/)

This package only supports the latest patch release of Python.

## Dependencies
- [requests](https://pypi.org/project/requests/)

## Installation
```bash
pip install binancetrader
```

## Example
Let's take a look at a quick example of using binancetrader package to send some simple orders over Jirnal system.

```python
from binancetrader import BinanceTrader as bint

client = bint(                                                               
            strat       = "gamma",
            address     = "You're given ip address",
            port        = 8000,
            api_key     = "You're given api tocken"
            )

client.marketOrder("BTCUSDT","BUY","0.001")                         #symbol,side,quantit
client.limitOrder("BTCUSDT","BUY","0.001","50000")                  #symbol,side,quantity,price
client.stopOrder("BTCUSDT","sell","0.001","40000")                  #symbol,side,quantity,price,stopPrice
client.takeProfitOrder("BTCUSDT","sell","0.001","60000")            #symbol,side,quantity,price,stopPrice
client.trailStopOrder("BTCUSDT","sell","0.001","55000","0.1")       #symbol,side,quantity,activationPrice,callbackRate
client.currentPositions("BTCUSDT")                                  #symbol
client.closeCurrentPositions("BTCUSDT")                             #symbol
client.currentOrders("BTCUSDT")                                     #symbol
client.cancelOrder("BTCUSDT","19225478")                            #symbol,orderId
client.cancelAllOpenOrder("BTCUSDT")                                #symbol
client.lastTrades("BTCUSDT","1640475569000","1640512577000","10")   #symbol
client.futuresBalance("USDT")                                       #symbol(DOT,BTC,SOL,BNB,ETH,ADA,USDT,XRP,BUSD)
```


