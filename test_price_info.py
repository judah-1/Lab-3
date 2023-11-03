import price_info

price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def test_total_cost_shopping():
    test_arr = 1.2 * 5 + 1.4 * 5 + 6.50 * 1 + 2.70 * 2 + 0.90 * 10 + 2.95 * 1 + 4.95 * 2
    result = price_info.total_cost_shopping(quantity_list, price_list)

    assert result == test_arr

def test_cost_of_fruit():
    test = 1.4*20
    result = price_info.cost_of_fruits("orange", 20)

    assert result == test