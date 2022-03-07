def init(params: dict):
    return None


def run(data: dict, func=None) -> bool:
    if data["objectPath"].startswith('cat'):
        return True
    if data["fileSize"] > 1*1024:
        return True
    return False


def teardown():
    pass
