import json
from json import JSONDecodeError

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.http import (
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    HttpResponse,
    JsonResponse,
)
from analysis.models import SolutionReport
from user.models import User
from problem.models import Solution, Problem, ProblemInput, ProblemOutput


def problem_view(request):
    if request.method == "GET":
        try :
            return JsonResponse(
                list(map(lambda problem: problem.to_dict(), Problem.objects.all())),
                status=200,
                safe=False,
            )
        except : return HttpResponseBadRequest()


    else:
        return HttpResponseNotAllowed(["POST", "UPDATE", "DELETE"])


def problem_by_id_view(request, problem_id=""):
    if request.method == "GET":
        try :
            problem = Problem.objects.get(pk=problem_id).to_dict()
            return JsonResponse(
                problem,
                status=200,
                safe=False,
            )
        except: return HttpResponseBadRequest()

    else:
        return HttpResponseNotAllowed(["POST", "UPDATE", "DELETE"])


def problem_by_objective_view(request, objective=""):
    if request.method == "GET":
        try:
            problem = Problem.objects.filter(objective=int(objective)).first().to_dict()
            return JsonResponse(problem, status=200, safe=False)
        except: 
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(["POST", "UPDATE", "DELETE"])


def problem_input_view(request, problem_id=""):
    if request.method == "GET":
        try :
            problem_inputs =  ProblemInput.objects.filter(problem__id=problem_id).first().to_dict()
        except :
            return HttpResponseBadRequest()
        return JsonResponse(problem_inputs, status=200, safe=False)
    else:
        return HttpResponseNotAllowed(["POST", "UPDATE", "DELETE"])


def problem_output_view(request, problem_input_id=""):
    if request.method == "GET":
        problem_outputs = ProblemOutput.objects.filter(problem_input__id=problem_input_id).first().to_dict()
        if len(problem_outputs) == 0:
            return HttpResponse(status=400)
        return JsonResponse(problem_outputs, status=200, safe=False)
    else:
        return HttpResponseNotAllowed(["POST", "UPDATE", "DELETE"])


@csrf_exempt
def solution_view(request, problem_id):
    if request.method == "POST":
        if request.user.is_anonymous:
            request.user = User.objects.all().first()
        try:
            problem = Problem.objects.get(pk=problem_id)
        except ObjectDoesNotExist:
            return HttpResponseBadRequest()

        try:
            body = request.body.decode()
            code = json.loads(body)["code"]
            erase_cnt = json.loads(body)["erase_cnt"]
            elapsed_time = json.loads(body)["elapsed_time"]
        except (KeyError, JSONDecodeError) as error:
            return HttpResponseBadRequest(error)

        solution = Solution(
            problem=problem, code=code, erase_cnt=erase_cnt, elapsed_time=elapsed_time)
        solution.save()

        SolutionReport(
            solution=solution, author=request.user, title=f"{problem.pid}_report", code=code
        ).save()

        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(["GET", "UPDATE", "DELETE"])
