from __future__ import division
import exchange
from fair_value import fvList

def trade(exchange):
	"""
	Should return a list of trades to do.
	"""
	trades = []

	#get fair values
	nokus = fvList['NOKUS']
	nokfh = fvList['NOKFH']
	print(fvList)
	if(nokus[0]==None or nokus[1]==None or nokfh[0]==None or nokfh[1]==None):
		return trades

	nokusFair = sum(nokus)/2
	nokfhFair = sum(nokfh)/2

	data = exchange.last_data
	if(data['type']!='book'):
		return trades
	symb = data['symbol']
	if(symb!='NOKUS' and symb!='NOKFH'):
		return trades
	#calculating the arbitrage
	bsymb = 'NOKUS'
	topFair = nokfhFair
	if nokusFair>nokfhFair:
		bsymb = 'NOKFH'
		topFair = nokusFair

	print(nokusFair + " " + nokfhFair)
	if(abs(nokfhFair-nokusFair)>2):
		if(data['symbol']==bsymb):
			for sell_price, size in data['sell']:
				#if we can buy the lower worth for under the fair value of the higher, then we will
				if sell_price < btick:
					trades.append(['BUY', bsymb, sell_price, size])
		trades.append(['SELL', bsymb, max(portfolio[NOKFH], 10)])