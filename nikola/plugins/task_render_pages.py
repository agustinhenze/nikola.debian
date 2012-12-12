from nikola.plugin_categories import Task
from nikola.utils import config_changed


class RenderPages(Task):
    """Render pages into output."""

    name = "render_pages"

    def gen_tasks(self):
        """Build final pages from metadata and HTML fragments."""
        kw = {
            "post_pages": self.site.config["post_pages"],
            "translations": self.site.config["TRANSLATIONS"],
            "filters": self.site.config["FILTERS"],
        }
        self.site.scan_posts()
        flag = False
        for lang in kw["translations"]:
            for wildcard, destination, template_name, _ in kw["post_pages"]:
                for task in self.site.generic_page_renderer(lang,
                    wildcard, template_name, destination, kw["filters"]):
                    task['uptodate'] = [config_changed({
                        1: task['uptodate'][0].config,
                        2: kw})]
                    task['basename'] = self.name
                    flag = True
                    yield task
        if flag is False:  # No page rendered, yield a dummy task
            yield {
                'basename': self.name,
                'name': 'None',
                'uptodate': [True],
                'actions': [],
            }
