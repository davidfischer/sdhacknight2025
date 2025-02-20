import logging

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from eyepop import EyePopSdk


pop_id = "6174fa7da22e44c1a1340242c9bd3e8e"

log = logging.getLogger(__file__)


class HomePageView(TemplateView):
    """Displays the homepage."""

    template_name = "sdhacknight/index.html"

    def asl_present(self, result):
        """I'm not proud of this but so it goes. With more time, it would be better."""
        result_str = str(result)
        if "thumb" in result_str:
            return True

        return False

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if settings.EYEPOP_SECRET_KEY and request.FILES["file"]:
            with EyePopSdk.workerEndpoint(
                pop_id=pop_id, secret_key=settings.EYEPOP_SECRET_KEY
            ) as endpoint:
                # Write file to disk temporarily
                fs = FileSystemStorage()
                fs.save(request.FILES["file"].name, request.FILES["file"])
                file_path = fs.location + "/" + request.FILES["file"].name

                log.info("Sending image (%s) to eyepop...", file_path)
                result = endpoint.upload(file_path).predict()
                log.info("Eyepop Result: %s", result)

                asl_present = self.asl_present(result)
                msg = "ASL not detected"
                if asl_present:
                    msg = "ASL detected!"
                context["result"] = msg
        else:
            context["result"] = "No file upload detected"

        return self.render_to_response(context)
