from graphene import ObjectType, relay
from graphene_django import DjangoObjectType

from fishes.models import Fish


class FishNode(DjangoObjectType):
    class Meta:
        model = Fish
        interfaces = (relay.Node,)


class FishConnection(relay.Connection):
    class Meta:
        node = FishNode


class Query(ObjectType):
    fish = relay.Node.Field(FishNode)
    all_fishes = relay.ConnectionField(FishConnection)

    def resolve_all_fishes(root, info, **kwargs):
        return Fish.objects.all()