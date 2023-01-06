from django.urls import path

from goals import views


urlpatterns = [
    path("goal_category/create", views.GoalCategoryCreateView.as_view(), name="goal_category_create"),
    path("goal_category/list", views.GoalCategoryListView.as_view(), name="goal_category_list"),
    path("goal_category/<pk>", views.GoalCategoryView.as_view(), name="goal_category_pk"),
    path("goal/create", views.GoalCreateView.as_view(), name="goal_create"),
    path("goal/list", views.GoalListView.as_view(), name="goal_list"),
    path("goal/<pk>", views.GoalView.as_view(), name="goal_pk"),
    path("goal_comment/create", views.GoalCommentCreateView.as_view(), name="goal_comment_create"),
    path("goal_comment/list", views.GoalCommentListView.as_view(), name="goal_comment_list"),
    path("goal_comment/<pk>", views.GoalCommentView.as_view(), name="goal_comment_pk"),
    path("board/create", views.BoardCreateView.as_view(), name="board_create"),
    path("board/list", views.BoardListView.as_view(), name="board_list"),
    path("board/<pk>", views.BoardView.as_view(), name="board_pk"),
]