from django.contrib.auth.models import Group
from django.http import JsonResponse


def tasks(request):
    data = {"tasks":[]}
    for group in Group.objects.all():
        data["tasks"].append(group.name)
    response = JsonResponse(data)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

    return response