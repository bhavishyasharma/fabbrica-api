import graphene

class Filter(graphene.InputObjectType):
    field = graphene.String()
    condition = graphene.String()
    value = graphene.String()

class Pagination(graphene.InputObjectType):
    page = graphene.Int()
    size = graphene.Int()


