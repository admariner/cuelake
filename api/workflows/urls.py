from django.urls import path
from . import views

urlpatterns = [
    path("workflows/<int:offset>", views.Workflows.as_view(), name="workflows"),
    path("workflows", views.Workflows.as_view(), name="workflowsPost"),
    path("workflowRuns/<int:workflowId>/<int:offset>", views.WorkflowRun.as_view(), name="workflowRuns"),
    path("workflowRuns/<int:workflowRunId>", views.WorkflowRunLog.as_view(), name="workflowRunLogs"),
    path("runWorkflow/<int:workflowId>", views.RunWorkflow.as_view(), name="runWorkflow"),
    path("stopWorkflow/<int:workflowId>", views.StopWorkflow.as_view(), name="stopWorkflow"),
]