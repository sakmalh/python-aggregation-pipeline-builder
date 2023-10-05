# Python Aggregation Pipeline Builder
Welcome to the MongoDB Python Aggregation Pipeline Builder repository! This powerful Python library empowers developers to construct and execute MongoDB aggregation pipelines with ease. With its intuitive and user-friendly API, you can create complex aggregation pipelines effortlessly, unleashing the full potential of MongoDB's aggregation framework.

# Key Features
- Concise and readable Python syntax for constructing MongoDB aggregation pipelines.
- Eliminate boilerplate code and reduce the number of lines needed to create powerful pipelines.
- Full support for MongoDB aggregation stages, allowing you to achieve sophisticated data processing with minimal code.

# Documentation
## Match
```python
pipeline.match(deleted_at={'$exists': 0})
```

## Lookup

```python
pipeline.look_up(from_collection='user', local_field='user', foreign_field='_id', as_field='user')
```

## Projection
```python
pipeline.project(id_project=0, id={'$toString': '$user._id'}, firstname='$user.first_name',
                 last_name='$user.last_name', email='$user.email')
```
## Regex or Other Query Selectors
```python
query_one = query_selectors.query_selector(f'user.first_name', regex=name, options='i')
```

## OR, AND and NOT
Can be provided as arguments or a single list.
```python
boolean.OR(or_list)
```

# Transformation

## Before
```json
[
   {
      "$match":{
         "deleted_at":{
            "$exists":0
         }
      }
   },
   {
      "$lookup":{
         "from":"user",
         "localField":"user",
         "foreignField":"_id",
         "as":"user"
      }
   },
   {
      "$unwind":{
         "path":"$user"
      }
   },
   {
      "$match":{
         "$or":[
            {
               "user.first_name":{
                  "$regex":"Joh",
                  "$options":"i"
               }
            },
            {
               "user.last_name":{
                  "$regex":"Joh",
                  "$options":"i"
               }
            },
            {
               "user.email":{
                  "$regex":"Joh",
                  "$options":"i"
               }
            }
         ]
      }
   },
   {
      "$limit":10
   },
   {
      "$project":{
         "_id":0,
         "id":{
            "$toString":"$user._id"
         },
         "firstname":"$user.first_name",
         "last_name":"$user.last_name",
         "email":"$user.email"
      }
   }
]
```

## After
```python
from pipeline_builder import AggregationQueryBuilder
from operators import query_selectors, boolean

name = 'Joh'
pipeline = AggregationQueryBuilder()
pipeline.match(deleted_at={'$exists': 0})
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
```

# Thanks 
We hope you find the MongoDB Python Aggregation Pipeline Builder helpful in simplifying your MongoDB data transformation tasks. Feel free to star the repository and provide feedback.

Happy coding! 🐍📊💡
