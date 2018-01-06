class main(object):
    def max_rise(self, data):
        maxm_rise = 0
        date = None
        for x in range(len(data) - 1):
            previous = float(data[x][1])
            current = float(data[x + 1][1])
            change = current - previous
            percentage = change / previous * 100
            if percentage > maxm_rise:
                maxm_rise = percentage
                date = data[x + 1][0]
        return (maxm_rise, date)

    def max_fall(self, data):
        maxm_fall = 0
        date = None
        for x in range(len(data) - 1):
            previous = float(data[x][1])
            current = float(data[x + 1][1])
            change = current - previous
            percentage = change / previous * 100
            if percentage < maxm_fall:
                maxm_fall = percentage
                date = data[x + 1][0]
        return (maxm_fall, date)
    
    def max_price(self, data):
        maxm_price = 0
        maxm_price_date = None
        for x in range(len(data) - 1):
            price = float(data[x][1])
            date = data[x][0]
            if price > maxm_price:
                maxm_price = price
                maxm_price_date = date
        return (maxm_price, maxm_price_date)

