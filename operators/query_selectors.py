def query_selector(field, **kwargs):
    selector_options = {}
    for keys in kwargs:
        temp_keys = '$' + keys
        selector_options[temp_keys] = kwargs[keys]

    return {field: selector_options}
