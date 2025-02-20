import logging

from django.views.generic import TemplateView


log = logging.getLogger(__file__)


class HomePageView(TemplateView):
    """Displays the homepage."""

    template_name = "sdhacknight/index.html"
