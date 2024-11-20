# Kalshi Trading System

## Requirements
- Python 3.10+
- Kalshi API key (prod and/or demo)
- Running Kafka server (see [here](https://kafka.apache.org/quickstart) for more information)
    - Assumes default port of 9092

## Installation

To install the required packages, run:

```bash
pip install -r requirements.txt
```

## Using the system

Once all requirements are met, make sure that all necessary environment variables (like API keys) are set before running the application.

The system will look for the following Kalshi API keys:
- `KALSHI_PROD_EMAIL`
- `KALSHI_PROD_PASSWORD`
- `KALSHI_DEMO_EMAIL`
- `KALSHI_DEMO_PASSWORD`

To switch between production and demo environments, change the `kalshi_api` variable in `KalshiAPI.py` to either `prod_kalshi_api` or `demo_kalshi_api`.

There are several services that can be run:
- `MarketDataService` 
    - Listens for market data events from Kalshi and pushes them to Kafka
- `MarketMonitor`
    - Listens for market data events from Kafka and passes them to any handlers that are passed in
    - `print_orderbook` is an example of a handler that prints the current state of the orderbook to the terminal
- User Strategies (`TestStrategy`)
    - Strategies are effectively event listeners that listen for market data events and do something with them, whether that's logging, sending orders, notifying a user, etc.
    - `TestStrategy` is a simple example of a strategy that listens for market data events and sends a market order to Kalshi under certain conditions
- `OrderManagementSystem`
    - Keeps track of open orders and positions sent from various strategies

- To run the relevant services, use the `run.py` script.
    - The `MarketDataService` is run automatically when this script is run
    - The `--components` flag allows you to specify which additional components to run
        - `monitor` will run the market monitor with `print_orderbook`, which will print the current state of the orderbook to the terminal
        - `strategy` will run the test strategy, which will listen for market data events and send a market order to Kalshi under certain conditions
- An example of how to run the system is:
    ```bash
    python run.py --components monitor strategy --ticker POPVOTEMOVSMALLER-24
    ```
    - This will run the market data service, and the market monitor with the test strategy
- If you don't specify a ticker, the system will not automatically subscribe to markets in `market_list` as defined in `Series.py`