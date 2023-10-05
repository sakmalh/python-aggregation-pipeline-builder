from pipeline_builder import AggregationQueryBuilder
from operators import comparison, conditions, query_selectors, boolean

name = 'Joh'
pipeline = AggregationQueryBuilder()
pipeline.match(organization_id='organization_id', deleted_at={'$exists': 0})
pipeline.look_up(from_collection='user', local_field='user', foreign_field='_id', as_field='user')
pipeline.unwind(path='user')
if name and name != "":
    list_query = ['first_name', 'last_name', 'email']
    or_list = []
    for query_field in list_query:
        query_one = query_selectors.query_selector(f'user.{query_field}', regex=name, options='i')
        or_list.append(query_one)
    pipeline.match(boolean.OR(or_list))
pipeline.limit(10)
pipeline.project(id_project=0, id={'$toString': '$user._id'}, firstname='$user.first_name',
                 last_name='$user.last_name', email='$user.email')
print(pipeline.get_query())
