from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PublishingPanel,
    FieldRowPanel,
    InlinePanel
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting
)

from wagtail.fields import RichTextField

from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin
)

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtail.contrib.forms.panels import FormSubmissionsPanel

from wagtail.snippets.models import register_snippet


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name="form_fields")


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address'),
                FieldPanel('to_address'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


@register_snippet
class FooterText(DraftStateMixin, RevisionMixin, PreviewableMixin, TranslatableMixin, models.Model):
    body = RichTextField()
    panels = [FieldPanel("body"), PublishingPanel()]

    def __str__(self) -> str:
        return "Footer text"
    
    def get_preview_template(self, request, mode_name):
        return "base.html"
    
    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"




@register_setting
class NavigationSettings(BaseGenericSetting):
    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    mastodon_url = models.URLField(verbose_name="Mastodon URL", blank=True)
    youtube_url = models.URLField(verbose_name="YouTube URL", blank=True)
    twitch_url = models.URLField(verbose_name="Twitch URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("mastodon_url"),
                FieldPanel("youtube_url"),
                FieldPanel("twitch_url"),
            ],
            "Social Settings",
        )
    ]




# Create your models here.
