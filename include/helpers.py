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
