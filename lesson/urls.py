from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy

app_name = 'lesson'


class MyHackedView(auth_view.PasswordResetView):
    success_url = reverse_lazy('lesson:password_reset_done')


urlpatterns = [
    # path('', views.all_materials, name='all_materials'),
    path('', views.MaterialListView.as_view(), name='all_materials'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',
         views.material_details,
         name='material_details'),
    path('<int:material_id>/share/', views.share_material,
         name='share_material'),
    path('create/', views.create_form, name='create_form'),
    # path('login/', views.user_login, name='login'),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    # path('password_reset/', auth_view.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/', MyHackedView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(success_url=reverse_lazy('lesson:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
