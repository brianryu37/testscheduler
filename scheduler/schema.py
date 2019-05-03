import graphene
from graphene_django.types import DjangoObjectType
from .models import Student,Instructor,Course

class InstructorType(DjangoObjectType):
    class Meta:
        model = Instructor

class CourseType(DjangoObjectType):
    class Meta:
        model = Course
    
class Query(graphene.ObjectType):
    instuctors = graphene.List(InstructorType)
    courses = graphene.List(CourseType)

    def resolve_instructors(self,context):
        return Instructor.objects.all()

    def resolve_movies(self,context):
        return Courses.objects.all()

schema = graphene.Schema(query=Query)
