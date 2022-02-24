from django.http import HttpResponse
from django.views.generic import View

def index(request):
    return HttpResponse("Hello, world. You're at the invitation index.")

class InvitationsView(View):

    def get(self, request, id):
        return HttpResponse(f"It's GET of {self.kwargs['id']}.")

    def post(self, request, id):
        return HttpResponse(f"It's POST of {self.kwargs['id']}.")