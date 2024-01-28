from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_INTEGER, TYPE_STRING


class UserSchema:
    def all(self):
        page = Parameter('page', IN_QUERY, type=TYPE_INTEGER, default=1)
        per_page = Parameter('per_page', IN_QUERY,
                             type=TYPE_INTEGER, default=10)
        query = Parameter('q', IN_QUERY, type=TYPE_STRING)
        return [page, per_page, query]
