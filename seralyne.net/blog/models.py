from django.db import models
from django.shortcuts import render

from portfolio.blocks import PortfolioStreamBlock
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


import readtime


from django.db import models
from wagtail.search import index
from wagtail.fields import RichTextField



class BlogIndexPage(RoutablePageMixin, Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogPage.objects.live().public()
        return context

    @route(r'^$')
    def index_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['categories'] = BlogCategory.objects.all()
        return render(request, "blog/blog_index_page.html", context)
        pass
    
    @route(r'^tag/(?P<tag_slug>[-\w]*)/$', name="tag_view")
    def tag_view(self, request, tag_slug):
        """Find blog posts by tag"""
        context = self.get_context(request)
        context["tag"] = tag_slug
        context['posts'] = context['posts'].filter(tags__slug__in=[tag_slug])
        return render(request, "blog/blog_index_page.html", context)
    
    @route(r'^category/(?P<cat_slug>[-\w]*)/$', name="category_view")
    def category_view(self, request, cat_slug):
        """Find blog posts by tag"""
        context = self.get_context(request)
        try:
            category = BlogCategory.objects.get(slug=cat_slug)
        except Exception:
            category = None

        if category is None:
            pass


        context["category"] = category
        context['posts'] = BlogPage.objects.filter(categories__in=[category])
        return render(request, "blog/blog_index_page.html", context)
    





class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name="tagged_items",
        on_delete=models.CASCADE
    )


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, null=True)


    
    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
        FieldPanel('description'),
        FieldPanel('slug')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'


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
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.RelatedFields('tags', [index.SearchField('name', partial_match=True, boost=10)])
    ]

    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

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
        FieldPanel("tags"),
        FieldPanel("categories")
    ]




    