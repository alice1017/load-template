#!/usr/bin/env python
# coding: utf-8

import os
import shutil

from unittest import TestCase
from load_template.core import (
    TemplateLoader,
    TEMPLATE_DIR,
    DEFAULT_TEMPLATE_DIR
)


class TemplateLoaderTestCase(TestCase):

    def test_variables(self):

        self.assertEqual(
            TEMPLATE_DIR,
            "{}/.templates".format(os.environ["HOME"])
        )

        self.assertEqual(
            DEFAULT_TEMPLATE_DIR,
            os.path.abspath("templates")
        )

    def test_initalize(self):

        template_dir, default_dir = self._setup_testdir()

        loader = TemplateLoader(
            template_dir=template_dir,
            default_dir=default_dir
        )

        self.assertEqual(
            loader.templates_list,
            ["python"]
        )

        self.assertEqual(
            loader.templates_data,
            {"python": "#!/usr/bin/env python\n# coding: utf-8"}
        )

        self._teardown_testdir(template_dir, default_dir)

    def _setup_testdir(self):

        default_dir = "/tmp/load-template-default"
        template_dir = "/tmp/load-template"

        os.mkdir(default_dir)

        with open(os.path.join(default_dir, "python"), "w") as fp:
            fp.write("#!/usr/bin/env python\n# coding: utf-8")

        return template_dir, default_dir

    def _teardown_testdir(self, template_dir, default_dir):

        shutil.rmtree(template_dir)
        shutil.rmtree(default_dir)
