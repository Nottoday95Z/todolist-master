from django.urls import path

from . import views

urlpatterns = [
    path('goal_category/create', views.GoalCategoryCreateView.as_view()),
    path('goal_category/list', views.GoalCategoryListView.as_view()),
    path('goal_category/<pk>', views.GoalCategoryView.as_view()),
    path('goal/create', views.GoalCreateView.as_view()),
    path('goal/list', views.GoalListView.as_view()),
    path('goal/<pk>', views.GoalView.as_view()),
    path('goal_comment/create', views.GoalCommentCreateView.as_view()),
    path('goal_comment/list', views.GoalCommentListView.as_view()),
    path('goal_comment/<pk>', views.GoalCommentView.as_view()),
    path('board/create', views.BoardCreateView.as_view()),
    path('board/list', views.BoardListView.as_view()),
    path('board/<pk>', views.BoardView.as_view()),
]