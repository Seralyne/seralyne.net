from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from portfolio.blocks import PortfolioStreamBlock

from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class HomePage(Page):
    # Add the hero section of the homepage
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )

    hero_text = models.CharField(blank=True, max_length=255, help_text="Write a big bold first impression for the site")
    hero_subtext = models.CharField(blank=True, max_length=255, help_text="Write a subtitle for the site")
    hero_cta = models.CharField(blank=True, max_length=255, help_text="Text to display on call to action")
    hero_cta_link = models.ForeignKey("wagtailcore.Page", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", 
                                      verbose_name="Hero CTA link", help_text="Choose a page to link to for the call to action", )
    hero_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage hero section background image",
        blank=True
        )
    
    

    
    body = StreamField(
        PortfolioStreamBlock(),
        blank=True,
        use_json_field=True,
        help_text = "Body",
    )
        

    # modify your content panels

    content_panels= Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_subtext"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
                FieldPanel("hero_background_image"),
            ],
            heading="Hero section"
        ),
        FieldPanel("body"),
    ]

    pass
