import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType

from .models import Puzzle


class PuzzleType(DjangoObjectType):
    class Meta:
        model = Puzzle


class Query(graphene.ObjectType):
    puzzles = graphene.List(PuzzleType)

    def resolve_puzzles(self, info, **kwargs):

        return Puzzle.objects.all()


class CreatePuzzle(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    title = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, title, description):
        user = info.context.user or None

        puzzle = Puzzle(
            url=url,
            title=title,
            description=description,
            posted_by=user,
        )
        puzzle.save()

        return CreatePuzzle(
            id=puzzle.id,
            url=puzzle.url,
            title=puzzle.title,
            description=puzzle.description,
            posted_by=puzzle.posted_by,
        )


class Mutation(graphene.ObjectType):
    create_puzzle = CreatePuzzle.Field()