class AggregationQueryBuilder(object):
    def __init__(self):
        self.query = []

    def get_query(self):
        return self.query

    def add_raw(self, raw):
        if type(raw) == list:
            self.query += raw
        if type(raw) == dict:
            self.query.append(raw)
        return self

    def limit(self, limit):
        self.query.append({'$limit': limit})
        return self

    def skip(self, skip):
        self.query.append({'$skip': skip})
        return self

    def project(self, id_project=None, exist=None, non_exist=None, **kwargs):
        projection = {}

        if id is not None:
            projection['_id'] = id_project

        if exist:
            for arg in exist:
                projection[arg] = 1

        if non_exist:
            for arg in non_exist:
                projection[arg] = 0

        for kwarg in kwargs:
            temp = kwarg.replace('__', '.')
            projection[temp] = kwargs[kwarg]

        self.query.append({
            '$project': projection
        })

        return self

    def match(self, query_dict=None, **query):
        if query_dict:
            self.query.append({'$match': query_dict})
        else:
            self.query.append({'$match': query})
        return self

    def group(self, id_group=None, **kwargs):
        if type(id_group) == str:
            if not id_group.startswith('$'):
                id_group = '$' + id_group
        query = {
            '_id': id_group
        }
        for key in kwargs:
            query[key] = kwargs[key]
        self.query.append({
            '$group': query
        })
        return self

    def unwind(self, path, include_array_index=None, preserve_null_and_empty_arrays=False):
        unwind_query = {'path': path if path[0] == '$' else '$' + path}

        if include_array_index:
            unwind_query['includeArrayIndex'] = include_array_index
        if preserve_null_and_empty_arrays:
            unwind_query['preserveNullAndEmptyArrays'] = True
        self.query.append({'$unwind': unwind_query})
        return self

    def sort(self, **kwargs):
        query = {}
        for field in kwargs:
            query[field] = kwargs[field]
        self.query.append({'$sort': query})
        return self

    def look_up(self, from_collection, local_field, foreign_field, as_field):
        query = {
            'from': from_collection,
            'localField': local_field,
            'foreignField': foreign_field,
            'as': as_field
        }
        self.query.append({'$lookup': query})
        return self

    def add_fields(self, **fields):
        query = {}
        for field in fields:
            query[field] = fields[field]
        self.query.append({'$addFields': query})
        return self

    def __str__(self):
        return str(self.query)

