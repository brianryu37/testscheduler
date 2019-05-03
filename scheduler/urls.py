from django.contrib import admin
from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .schema import schema

urlpatterns = [
    # /scheduler/
    path('', views.index, name='index'),

    # /scheduler/instructor
    path('<class_id>/', views.detail, name = 'detail'),

    # /scheduler/courses
    path('scheduler/courses/', views.show_courses, name = 'show_courses'),

    # /scheduler/add_courses
    path('add_course', views.add_courses, name = 'add_courses'),

    # /scheduler/instructors
    path('instructors', views.show_instructors, name = 'show_instructors'),

    # /sheduler/edit_i
    path('courses/<int:course_id>/edit_instructors/', views.edit_instructors, name = 'edit_instructors'),

    # /scheduler/add_instructor
    path('add_instructor', views.add_instructor, name='add_instructor'),

    path('courses/<int:course_id>/delete', views.delete, name = 'delete'),

    path('graphql/',csrf_exempt(GraphQLView.as_view(
        graphiql=True,
        schema=schema
    ))),

]
