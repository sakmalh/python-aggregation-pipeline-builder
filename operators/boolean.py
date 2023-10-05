def AND(*expressions):
    if type(expressions[0]) is list:
        return {'$and': expressions[0]}
    return {'$and': list(expressions)}


def OR(*expressions):
    if type(expressions[0]) is list:
        return {'$or': expressions[0]}
    return {'$or': list(expressions)}


def NOT(*expressions):
    if type(expressions[0]) is list:
        return {'$not': expressions[0]}
    return {'$not': list(expressions)}