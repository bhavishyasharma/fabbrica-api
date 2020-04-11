def filter_qs(qs, filters):
    if filters is not None:
        filter = {}
        for f in filters:
            filter[f.field+"__"+f.condition] = f.value
        qs = qs.objects(**filter)
    return qs

def pagination_qs(qs, pagination):
    if pagination is not None:
        first = pagination.page * pagination.size
        qs = qs[first: first+pagination.size]
    return qs

def sortings_qs(qs, sortings):
    if sortings is not None:
        qs = qs.order_by(*sortings)
    return qs