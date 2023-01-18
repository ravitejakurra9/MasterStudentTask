from django.urls import path

from MasterStudentApp import views

urlpatterns=[
    path('',views.index_fun,name='home'),
    path('masterlog',views.masterlog_fun,name='mlog'),
    path('masterreg',views.masterreg_fun,name='mreg'),
    path('studentlog',views.studentlog_fun,name='slog'),
    path('studentreg',views.studentreg_fun,name='sreg'),
    path('a_task',views.a_task_fun,name='a_task'),
    # path('taskdata',views.taskdata_fun),
    path('solve/<int:id>',views.slove_fun,name='sol'),
    path('alltask',views.viewalltask_fun,name='alltask'),
    path('student_pending/<int:sid>',views.sp_fun,name='sp'),
    path('student_completed/<int:sid>',views.sc_fun,name='sc'),
    path('std_home/<int:sid>',views.std_home_fun,name='std_home'),
    path('test',views.test_fun)


]