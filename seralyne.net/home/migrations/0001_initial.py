# Generated by Django 5.0.8 on 2024-08-18 17:05

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero_text', models.CharField(blank=True, help_text='Write a big bold first impression for the site', max_length=255)),
                ('hero_subtext', models.CharField(blank=True, help_text='Write a subtitle for the site', max_length=255)),
                ('hero_cta', models.CharField(blank=True, help_text='Text to display on call to action', max_length=255)),
                ('col_one', wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('embed_block', 7), ('card', 11), ('featured_posts', 15)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a heading size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert a URL to embed. For example, a YouTube URL.', 'icon': 'media'}), 8: ('wagtail.blocks.CharBlock', (), {}), 9: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic', 'link']}), 10: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 11: ('wagtail.blocks.StructBlock', [[('heading', 8), ('text', 9), ('image', 10)]], {'group': 'Sections'}), 12: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic', 'link'], 'required': False}), 13: ('wagtail.blocks.PageChooserBlock', (), {'page_type': ['blog.BlogPage']}), 14: ('wagtail.blocks.ListBlock', (13,), {}), 15: ('wagtail.blocks.StructBlock', [[('heading', 8), ('text', 12), ('posts', 14)]], {'group': 'Sections'})}, help_text='Column 1')),
                ('col_two', wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('embed_block', 7), ('card', 11), ('featured_posts', 15)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a heading size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert a URL to embed. For example, a YouTube URL.', 'icon': 'media'}), 8: ('wagtail.blocks.CharBlock', (), {}), 9: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic', 'link']}), 10: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 11: ('wagtail.blocks.StructBlock', [[('heading', 8), ('text', 9), ('image', 10)]], {'group': 'Sections'}), 12: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic', 'link'], 'required': False}), 13: ('wagtail.blocks.PageChooserBlock', (), {'page_type': ['blog.BlogPage']}), 14: ('wagtail.blocks.ListBlock', (13,), {}), 15: ('wagtail.blocks.StructBlock', [[('heading', 8), ('text', 12), ('posts', 14)]], {'group': 'Sections'})}, help_text='Column 2')),
                ('col_three', wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('embed_block', 7), ('card', 11), ('featured_posts', 15)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a heading size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert a URL to embed. For example, a YouTube URL.', 'icon': 'media'}), 8: ('wagtail.blocks.CharBlock', (), {}), 9: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic', 'link']}), 10: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 11: ('wagtail.blocks.StructBlock', [[('heading', 8), ('text', 9), ('image', 10)]], {'group': 'Sections'}), 12: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic', 'link'], 'required': False}), 13: ('wagtail.blocks.PageChooserBlock', (), {'page_type': ['blog.BlogPage']}), 14: ('wagtail.blocks.ListBlock', (13,), {}), 15: ('wagtail.blocks.StructBlock', [[('heading', 8), ('text', 12), ('posts', 14)]], {'group': 'Sections'})}, help_text='Column 3')),
                ('hero_cta_link', models.ForeignKey(blank=True, help_text='Choose a page to link to for the call to action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Hero CTA link')),
                ('image', models.ForeignKey(help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
