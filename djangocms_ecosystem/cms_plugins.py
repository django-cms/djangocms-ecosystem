from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import gettext_lazy as _

from djangocms_ecosystem import get_chapter, read_ecosystem


@plugin_pool.register_plugin
class CMSPackagesPlugin(CMSPluginBase):
    render_template = "djangocms_ecosystem/packages.html"
    name = _("Official CMS packages")
    show_add_form = False

    def render(self, context, instance, placeholder):
        context.update({
            "content": get_chapter("CMS packages").get("content", []),
        })
        return context


@plugin_pool.register_plugin
class DjangoPackagesPlugin(CMSPluginBase):
    render_template = "djangocms_ecosystem/packages.html"
    name = _("Official Django packages")
    show_add_form = False

    def render(self, context, instance, placeholder):
        context.update({
            "content": get_chapter("Django packages").get("content", []),
        })
        return context


@plugin_pool.register_plugin
class DeprecatedPackagesPlugin(CMSPluginBase):
    render_template = "djangocms_ecosystem/deprecated.html"
    name = _("Deprecated packages")
    show_add_form = False

    def render(self, context, instance, placeholder):
        deprecated = [
            package
            for chapter in read_ecosystem()
            for package in chapter.get("content", [])
            if package.get("properties", {}).get("deprecated", False)
        ]
        context.update({"content": deprecated})
        return context