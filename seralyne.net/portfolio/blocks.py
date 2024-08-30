from base.blocks import BaseStreamBlock

from wagtail.blocks import (
    CharBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StructBlock
)

from wagtail.images.blocks import ImageChooserBlock


class CardBlock(StructBlock):
    heading = CharBlock()
    text = RichTextBlock(features=["bold", "italic", "link"])
    image=ImageChooserBlock(required=False)

    class Meta:
        icon = "form"
        template = "portfolio/blocks/card_block.html"

class ThreeColumnsBlock(StructBlock):
    heading = CharBlock()
    text = RichTextBlock(features=["bold", "italic", "link"], required=False)
    col_one = RichTextBlock(features=["bold", "italic", "link"], required=False)
    col_two = RichTextBlock(features=["bold", "italic", "link"], required=False)
    col_three = RichTextBlock(features=["bold", "italic", "link"], required=False)

    class Meta: 
        icon = 'doc-full-inverse'
        template = 'portfolio/blocks/three_columns_block.html'

class FeaturedPostsBlock(StructBlock):
    heading = CharBlock()
    text = RichTextBlock(features=["bold", "italic", "link"], required=False)
    posts = ListBlock(PageChooserBlock(page_type='blog.BlogPage'))

    class Meta:
        icon = 'folder-open-inverse'
        template = 'portfolio/blocks/featured_posts_block.html'




class PortfolioStreamBlock(BaseStreamBlock):
    card = CardBlock(group="Sections")
    featured_posts = FeaturedPostsBlock(group="Sections")
    three_columns_block=ThreeColumnsBlock(group="Sections")