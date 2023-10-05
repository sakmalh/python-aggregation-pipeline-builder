def COND(_if, _then, _else=None):
    condition = {'if': _if, 'then': _then}

    if _else is not None:
        condition['else'] = _else

    return {'$cond': condition}
