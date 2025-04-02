from django.views.generic import TemplateView


class AboutProjectView(TemplateView):
    """
        Static page that contains general information about project
    """
    template_name = 'static_pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О проекте'
        context['main_text'] = 'Данный проект помогает работникам общепита эффективно управлять своими заказами.'

        return context
