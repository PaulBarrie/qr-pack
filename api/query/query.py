from graphene import ObjectType, Field
from models.Container import Container


class Query(ObjectType):
    get_container = Field(Container)


    async def resolve_get_container(self, info):
        return {}
