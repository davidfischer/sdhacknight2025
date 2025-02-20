import logging

from django.conf import settings
from django.views.generic import TemplateView
from eyepop import EyePopSdk


pop_id = "6174fa7da22e44c1a1340242c9bd3e8e"

log = logging.getLogger(__file__)


class HomePageView(TemplateView):
    """Displays the homepage."""

    template_name = "sdhacknight/index.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if settings.EYEPOP_SECRET_KEY:
            with EyePopSdk.workerEndpoint(
                pop_id=pop_id, secret_key=settings.EYEPOP_SECRET_KEY
            ) as endpoint:
                result = endpoint.upload(request.FILES["file"]).predict()
                context["result"] = result
        else:
            context["result"] = "No file upload detected"

        return self.render_to_response(context)
