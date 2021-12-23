def init(params: dict):
    return None


def run(data: dict, func=None) -> bool:
    if data["objectPath"].startswith "207":
        return True
    if data["size"]>2*1024*1024:
        return True
    return False


def teardown():
    pass
