# theater.py
#
# The owner of a monopolistic movie theater in a small town has
# complete freedom in setting ticket prices.  The more he charges, the
# fewer people can afford tickets.  The less he charges, the more it
# costs to run a show because attendance goes up.  In a recent
# experiment the owner determined a relationship between the price of
# a ticket and average attendance.
#
# At a price of $5.00/ticket, 120 people attend a performance.  For
# each 10-cent change in the ticket price, the average attendance
# changes by 15 people.  That is, if the owner charges $5.10, some 105
# people attend on the average; if the price goes down to $4.90,
# average attendance increases to 135.
#
# Unfortunately, the increased attendance also comes at an increased
# cost.  Every performance comes at a fixed cost of $180 to the owner
# plus a variable cost of $0.04 per attendee.
#
# The owner would like to know the exact relationship between profit
# and ticket price in order to maximize the profit.
#
# Write a program to figure out the best ticket price (to the nearest
# 10 cents) that maximizes profit.
#
# Credit: This problem comes from "How to Design Programs", 2nd Ed.


# 5.00, 120
# 5.10, 105
# 4.90, 135

# Flat cost: 180
# pp cost: 0.04

import numpy as np

def calc_cost(attendees):
    return 180 + 0.04*attendees


def calc_revenue(ticket_price, attendees):
    return ticket_price*attendees


def calc_profit(ticket_price):
    attendees = calc_attendees(ticket_price)
    cost = calc_cost(attendees)
    revenue = calc_revenue(ticket_price, attendees)
    profit = revenue - cost

    return profit, attendees


def calc_attendees(ticket_price):
    return 120 + ((5.00 - ticket_price)/0.10)*15


def generate_ticket_price():
    for row in np.arange(0.0, 100.0, 0.1):
        yield row


def main():
    max_profit = 0
    max_profit_attendees = 0
    max_ticket_price = 0

    gen = generate_ticket_price()

    for x in gen:
        profit, attendees = calc_profit(x)
        if profit > max_profit:
            max_profit = profit
            max_profit_attendees = attendees
            max_ticket_price = x

    print(max_profit, max_profit_attendees, max_ticket_price)


if __name__ == '__main__':
    main()
