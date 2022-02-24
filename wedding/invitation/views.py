import json
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import InvitedPerson


def index(request):
    return HttpResponse("Hello, world. You're at the invitation index.")


@method_decorator(csrf_exempt, name='dispatch')
class InvitationsView(View):

    def get(self, request, id):
        person = get_object_or_404(InvitedPerson, id=id)
        person.visit_count += 1
        person.save()

        return JsonResponse(person.to_dict())


    def patch(self, request: HttpRequest, id):
        if request.method != "PATCH":
            raise HttpResponseNotAllowed(["PATCH"])

        body = json.loads(request.body)
        if "decision" not in body:
            raise HttpResponseBadRequest("Decision not found.")

        decision = body["decision"]
        if not isinstance(decision, bool):
            raise HttpResponseBadRequest("Decision must be boolean.")

        person = get_object_or_404(InvitedPerson, id=id)
        person.decision = decision
        person.save()

        return JsonResponse(person.to_dict())
