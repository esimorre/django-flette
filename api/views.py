from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import redirect


def data(request):
    response = JsonResponse({"text": "text from django json api"})
    """response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    """
    return response


def flet_client(request):
    return redirect("/static/web/index.html")

def tasks(request):
    data = {"tasks":[]}
    for group in Group.objects.all():
        data["tasks"].append(group.name)

    response = JsonResponse(data)
    """response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    """
    return response