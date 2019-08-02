from termcolor import colored

from .._constants import NAME, VERSION, ExitCodes
from .._logic import get_installed, get_plugin_rules
from .._patched import FlakeHellApplication
from .._types import CommandResult


def installed_command(argv) -> CommandResult:
    app = FlakeHellApplication(program=NAME, version=VERSION)
    plugins = sorted(get_installed(app=app), key=lambda p: p['name'])
    if not plugins:
        return ExitCodes.NO_PLUGINS_INSTALLED, 'no plugins installed'

    width = max(len(p['name']) for p in plugins)
    template = '{name} | {codes:8} | {rules}'
    print(template.format(
        name=colored('NAME'.ljust(width), 'yellow'),
        codes=colored('CODES   ', 'yellow'),
        rules=colored('RULES', 'yellow'),
    ))
    for plugin in plugins:
        rules = get_plugin_rules(
            plugin_name=plugin['name'],
            plugins=app.options.plugins,
        )
        colored_rules = []
        for rule in rules:
            if rule[0] == '+':
                rule = colored(rule, 'green')
            elif rule[0] == '-':
                rule = colored(rule, 'red')
            colored_rules.append(rule)
        color = 'green' if rules else 'red'
        print(template.format(
            name=colored(plugin['name'].ljust(width), color),
            codes=', '.join(plugin['codes']),
            rules=', '.join(colored_rules),
        ))
    return 0, ''