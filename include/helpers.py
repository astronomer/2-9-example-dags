from sys import getsizeof


def set_up_report_platform():
    pass


def execute_report_mailer():
    pass


def tear_down_report_platform():
    pass


def deep_getsizeof(o, ids):
    """Find the size of an object including objects referenced by it"""
    if id(o) in ids:
        return 0

    r = getsizeof(o)
    ids.add(id(o))

    if isinstance(o, str) or isinstance(o, bytes):
        return r

    if isinstance(o, dict):
        return r + sum(
            deep_getsizeof(k, ids) + deep_getsizeof(v, ids) for k, v in o.items()
        )

    if hasattr(o, "__dict__"):
        return r + deep_getsizeof(o.__dict__, ids)

    if hasattr(o, "__iter__") and not isinstance(o, (str, bytes, bytearray)):
        return r + sum(deep_getsizeof(i, ids) for i in o)

    return r


def get_display_fruit(fruit_name):

    if fruit_name == "Strawberry":
        display_fruit = "🍓"
    elif fruit_name == "Banana":
        display_fruit = "🍌"
    elif fruit_name == "Tomato":
        display_fruit = "🍅"
    elif fruit_name == "Pear":
        display_fruit = "🍐"
    elif fruit_name == "Kiwi":
        display_fruit = "🥝"
    elif fruit_name == "Pineapple":
        display_fruit = "🍍"
    elif fruit_name == "Orange":
        display_fruit = "🍊"
    elif fruit_name == "GreenApple":
        display_fruit = "🍏"
    elif fruit_name == "Watermelon":
        display_fruit = "🍉"
    elif fruit_name == "Lemon":
        display_fruit = "🍋"
    elif fruit_name == "Mango":
        display_fruit = "🥭"
    elif fruit_name == "Blueberry":
        display_fruit = "🫐"
    elif fruit_name == "Apple":
        display_fruit = "🍎"
    elif fruit_name == "Melon":
        display_fruit = "🍈"
    elif fruit_name == "Grape":
        display_fruit = "🍇"
    elif fruit_name == "Avocado":
        display_fruit = "🥑"
    elif fruit_name == "Cherry":
        display_fruit = "🍒"
    elif fruit_name == "Peach":
        display_fruit = "🍑"
    elif fruit_name == "Hazelnut":
        display_fruit = "🌰"
    elif fruit_name == "Pumpkin":
        display_fruit = "🎃"
    else:
        display_fruit = ""

    return display_fruit
