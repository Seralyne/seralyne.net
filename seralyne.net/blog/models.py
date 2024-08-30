from django.db import models

from portfolio.blocks import PortfolioStreamBlock
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
import readtime


from django.db import models
from wagtail.search import index
from wagtail.fields import RichTextField



class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

class BlogPage(Page):


    def get_readtime(self):
        result = readtime._of_text(self.body)
        return result.text
    


    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField(
        PortfolioStreamBlock(),
        blank=True,
        use_json_field=True,
        help_text = "Use this section to list your projects and skills.",
    )
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body')
    ]

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Thumbnail",
    )

 

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("image"),
        FieldPanel("body"),
    ]
