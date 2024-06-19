'''
{
    "name": "Purchase Orders",
    "purchaseOrders": [
        {
            "id": "DD-2-P",
            "cost": 41.46
        },
        {
            "id": "DD-8-P",
            "cost": 18.59
        },
        {
            "id": "CC-1-C",
            "cost": 29.05
        },
        {
            "id": "AA-4-C",
            "cost": 25.86
        },
        {
            "id": "CC-5-C",
            "cost": 37.38
        },
        {
            "id": "BB-0-C",
            "cost": 15.66
        },
        {
            "id": "AA-2-P",
            "cost": 37.98
        },
        {
            "id": "BB-1-P",
            "cost": 50.6
        },
        {
            "id": "CC-7-P",
            "cost": 36.39
        },
        {
            "id": "BB-5-C",
            "cost": 41.3
        },
        {
            "id": "DD-6-C",
            "cost": 49.08
        },
        {
            "id": "AA-3-P",
            "cost": 11.03
        },
        {
            "id": "BB-6-P",
            "cost": 20.29
        },
        {
            "id": "DD-11-P",
            "cost": 27.79
        },
        {
            "id": "CC-10-P",
            "cost": 46.47
        },
        {
            "id": "BB-3-P",
            "cost": 46.4
        },
        {
            "id": "DD-7-P",
            "cost": 43.22
        },
        {
            "id": "AA-1-P",
            "cost": 29.26
        },
        {
            "id": "DD-4-P",
            "cost": 37.05
        },
        {
            "id": "BB-4-C",
            "cost": 48.34
        },
        {
            "id": "CC-4-P",
            "cost": 34.39
        },
        {
            "id": "DD-3-C",
            "cost": 18.76
        },
        {
            "id": "DD-5-C",
            "cost": 15.75
        },
        {
            "id": "AA-5-C",
            "cost": 11.59
        },
        {
            "id": "DD-1-P",
            "cost": 25.47
        },
        {
            "id": "BB-2-C",
            "cost": 31.39
        },
        {
            "id": "DD-0-P",
            "cost": 46.13
        },
        {
            "id": "CC-2-P",
            "cost": 23.22
        },
        {
            "id": "CC-6-P",
            "cost": 48.63
        },
        {
            "id": "CC-3-C",
            "cost": 16.99
        },
        {
            "id": "CC-9-C",
            "cost": 47.47
        },
        {
            "id": "CC-8-P",
            "cost": 13.42
        },
        {
            "id": "DD-9-P",
            "cost": 12.24
        },
        {
            "id": "CC-0-C",
            "cost": 26.85
        },
        {
            "id": "DD-10-C",
            "cost": 46.91
        },
        {
            "id": "AA-0-P",
            "cost": 39.37
        }
    ]
}

- fetch the data from the url
    URL: "https://mf-public-demo-files.s3.amazonaws.com/pos.json" OK

- response its length of purchaseOrder OK

'''

# "id": "BB-1-P",

from collections import defaultdict
from requests import get


def fetch_purchase_order(url: str = "https://mf-public-demo-files.s3.amazonaws.com/pos.json") -> list:
    data = get(url, timeout=10).json()
    return data["purchaseOrders"]


def count_purchase_orders(data: list) -> int:
    return len(data)


def sort_costs(purchase_data: list):
    result = []
    for data in purchase_data:
        result.append(data['cost'])

    return sorted(result, reverse=True)


def get_vendor_code(purchase: dict):
    return purchase["id"].split("-")[0]


def get_cost(item: dict):
    return item["cost"]


def scratch_method(purchase_data):
    output = defaultdict(list)
    for item in purchase_data:
        output[get_vendor_code(item)].append(item)

    for vendor, cost in sorted(output.items()):
        costs = sort_costs(cost)
        print(output[vendor])
        for order in output[vendor]:
            cost = get_cost(order)
            print(cost)

    return output


def group_data(data):
    vendor_orders = {}
    for order in data:
        # Extract vendor code from the id
        vendor = order['id'].split('-')[0]

        # If the vendor is not in the dictionary, add an empty list
        if vendor not in vendor_orders:
            vendor_orders[vendor] = []

        # Append the order id and cost as a tuple to the vendor's list
        vendor_orders[vendor].append((order['id'], order['cost']))

        # Sort each vendor's orders by cost in descending order
        for vendor in vendor_orders:
            vendor_orders[vendor].sort(key=lambda x: x[1], reverse=True)

        # Create a new dictionary with the vendors in the specified order
        sorted_vendor_orders = {}
        vendor_order = ['AA', 'BB', 'CC', 'DD']
        for vendor in vendor_order:
            if vendor in vendor_orders:
                sorted_vendor_orders[vendor] = vendor_orders[vendor]

    # Print the total number of purchase orders
    total_orders = sum(len(orders) for orders in vendor_orders.values())
    print("Total number of purchase orders:", total_orders)

    # Print the sorted vendor orders
    return sorted_vendor_orders


data = fetch_purchase_order()

result = group_data(data)
print(result)
