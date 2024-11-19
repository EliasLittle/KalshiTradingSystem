import logging
from MarketMonitor import monitor_event
from Series import event_list
from OrderBook import OrderBook
from OrderManagementSystem import OrderManagementSystem, Order
from KalshiAPI import demo_kalshi_api

oms = OrderManagementSystem(demo_kalshi_api)

# If the best no price is between 50 and 70, send a buy order for 10 contracts at (at most) the best no price + 5 cents
# WARNING: This strategy is not profitable and is only for demonstration purposes
def strategy(orderbook: OrderBook, updates: int, timestamp: float, logger: logging.Logger):
    if orderbook.best_no > 50 and orderbook.best_no < 70:
        oms.send_order(Order(
            ticker=orderbook.ticker,
            action="buy",
            type="limit",
            no_price=orderbook.best_no + 5,
            amount=10,
            side="no"
        ))

    logger.info(f"Orderbook: {orderbook}")

def main(logger: logging.Logger):
    event = event_list[0]
    monitor_event(event, strategy, logger)