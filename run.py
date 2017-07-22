import argparse
import time

import Exchange
import Bot


def main(strategies, test):
    exchange = Exchange(test)
    print "Connected to exchange"
    bot = Bot(exchange, strategies)
    print "Bot initialized"
    bot.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('strategies')
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    strategies = args.strategies.split(',')
    while True:
        try:
            main(strategies, args.test)
        except:
            # TODO metrics for each round
            time.sleep(1)
