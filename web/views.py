import requests
import logging

from django.conf import settings
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, DetailView, View

from web.models import Application, Post
from .forms import ApplicationForm

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


class HomePageView(TemplateView):
    template_name = "web/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()[:3]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "web/post_detail.html"
    context_object_name = "post"


class ApplicationCreateView(View):
    template_name = 'application_form.html'
    form_class = ApplicationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            application = Application.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone']
            )

            try:
                logger.info(f"Application created: {application}")
                self.send_telegram_message(application)
                return JsonResponse({
                    'success': True,
                    'message': _('Ваша заявка принята')
                })
            except Exception:
                logger.error('Error while sending telegram message')
                return JsonResponse({
                    'success': False,
                    'message': _('Произошла ошибка, попробуйте позже')
                })
        else:
            logger.error(f'Form is not valid: {form.errors}')
            return JsonResponse({
                'success': False,
                'message': _('Форма заполнена неверно. Попробуйте еще раз')
            })

    def send_telegram_message(self, application):
        telegram_token = settings.TELEGRAM_BOT_TOKEN
        telegram_chat_id = settings.TELEGRAM_CHAT_ID
        message = f"New Application from Web Site:\n\n- Name: {application.name}\n- Phone: {application.phone}"
        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        data = {
            'chat_id': telegram_chat_id,
            'text': message
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
