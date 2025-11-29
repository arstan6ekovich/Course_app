from rest_framework import routers
from django.urls import path, include
from .views import (UserProfileViewSet, CategoryViewSet, SubcategoryViewSet,
                    CourseViewSet, LessonViewSet, AssignmentViewSet,
                    ExamViewSet, QuestionViewSet, OptionViewSet,
                    CertificateViewSet, ReviewViewSet)


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'sub_categories', SubcategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'options', OptionViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
]