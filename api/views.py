# Create your views here.
from rest_framework.decorators import api_view
import api


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    :param request:
    :return:
    """
    if request.method == 'GET':
        snippets = api.objects.all()
