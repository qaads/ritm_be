get_users_schema = {
        "type": "object",
        "properties":{
            "page": {"type": "integer"}, # TODO: Какие могут быть значения?
            "per_page": {"type": "integer"}, # TODO: Какие могут быть значения?
            "total": {"type": "integer"}, # TODO: Какие могут быть значения?
            "total_pages": {"type": "integer"}, # TODO: Какие могут быть значения?
            "data": {"type": "array",
                     "items":{
                         "type": "object",
                         "properties":{
                            "id": {"type": "integer"},
                            "email": {"type": "string", "format": "email"},
                            "first_name": {"type": "string"},
                            "last_name": {"type": "string"},
                            "avatar": {"type": "string", "format": "uri"}
                         },
            },
            "required": ["page",
                         "per_page",
                         "total",
                         "total_pages",
                         "data"]}
}
}
