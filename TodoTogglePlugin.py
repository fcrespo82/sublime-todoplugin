import sublime, sublime_plugin
import re

class TodoToggleCommand(sublime_plugin.TextCommand):

    prefix = "- [ ] "

    checked = r"^(\s*[-*+]\s)\[x\]"
    unchecked = r"^(\s*[-*+]\s)\[\s?\]"
    list_item = r"^(\s*[-*+]\s)"

    def run(self, edit):
        view = self.view
        for region in view.sel():
            lines = view.split_by_newlines(region)
            for line_item in lines:
                line_region = view.line(line_item)
                line = view.substr(line_region)

                mc = re.match(self.checked, line, re.IGNORECASE)
                mu = re.match(self.unchecked, line, re.IGNORECASE)
                mli = re.match(self.list_item, line, re.IGNORECASE)

                if mc:
                    line = mc.expand(r"\1[ ]") + mc.string[mc.end():]
                elif mu:
                    line = mu.expand(r"\1[x]") + mu.string[mu.end():]
                elif mli:
                    line = mli.expand(r"\1[ ]") + mli.string[mli.end():]
                else:
                    line = self.prefix + line;
                print(line)

                view.replace(edit, line_region, line)
