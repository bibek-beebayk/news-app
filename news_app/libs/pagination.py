from rest_framework.pagination import PageNumberPagination as BasePageNumberPagination
from rest_framework.response import Response


class PageNumberPagination(BasePageNumberPagination):
    aggregate = None

    def get_paginated_response(self, data):
        return Response(self.get_response_data(data))

    def get_response_data(self, data):
        count = self.page.paginator.count
        size = self.page_size
        pagination = {
            'count': count,
            'page': self.page.number,
            'pages': (count + (-count % size)) // size,  # round-up division
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'size': size,
        }
        response_data = {
            'pagination': pagination,
            'results': data
        }
        if self.aggregate:
            response_data['aggregate'] = self.aggregate
        return response_data


def paginate(queryset, request, serializer_class, page_size=None):
    paginator = PageNumberPagination()
    if page_size:
        paginator.page_size = page_size
    page = paginator.paginate_queryset(queryset, request)
    context = {'request': request}
    serializer = serializer_class(page, many=True, context=context)
    paginated_response = paginator.get_paginated_response(serializer.data)
    data = paginated_response.data
    return data