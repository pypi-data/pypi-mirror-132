# whey-mixin

[![PyPI version](https://img.shields.io/pypi/v/whey-mixin.svg)](https://pypi.python.org/pypi/whey-mixin/)
[![PyPI status](https://img.shields.io/pypi/status/whey-mixin.svg)](https://pypi.python.org/pypi/whey-mixin/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/whey-mixin.svg)](https://pypi.python.org/pypi/whey-mixin/)
[![GitHub license](https://img.shields.io/github/license/logicplace/whey-mixin.svg)](https://github.com/logicplace/whey-mixin/blob/master/LICENSE)

A plugin for Whey build system to add simple build steps

## Usage

First, reassign your Whey builders to be handled by mixin. The following are supported, use as many or as few as you like.

```toml
[tool.whey.builders]
sdist = "whey_mixin_sdist"
wheel = "whey_mixin_wheel"
binary = "whey_mixin_binary"
exe = "whey_mixin_exe"
dmg = "whey_mixin_dmg"
deb = "whey_mixin_deb"
rpm = "whey_mixin_rpm"
```

Next, make the code for your hooks. We will place ours in a `build_hooks.py` file in the root directory of our project.

```py
from whey.mixin import BuilderMixin

def build_messages(self: BuilderMixin):
  # This makes Babel a build dep
  from babel.messages.mofile import write_mo
  from babel.messages.pofile import read_po

  # pkgdir is the base folder for your module, constructed from
  # the root folder, tool.whey.source-dir, and tool.whey.package
  locales = self.pkgdir / "locales"
  if self.verbose:
    print("  Building messages")

  # Find all .po files for all languages
  for po in locales.glob("*/LC_MESSAGES/*.po"):
    with po.open("rt", encoding="UTF-8") as f:
      # po.parts[-3] extracts the language part of the path
      # po.stem is the domain
      catalog = read_po(f, po.parts[-3], po.stem)

    # Here we construct the path relative to the build directory
    # (/build by default). Be sure to create the subdirs!
    mo = self.build_dir / po.relative_to(self.project_dir).with_suffix(".mo")
    mo.parent.maybe_make(parents=True)
    with mo.open("wb") as f:
      write_mo(f, catalog)

    # This reports to Whey they we've written a file, so that
    # it will include it in the final package
    self.report_written(mo)

    if self.verbose:
      print("    Wrote language file:", mo)
```

Next, configure whey-mixin itself. You can supply global or builder-specific hooks. You may also specify the base class to use per builder. By default, it uses Whey's default SDistBuilder for sdist, and its WheelBuilder for wheel and binary; there is no default for anything else, so those must be specified.

Make sure to add any dependencies into you build deps

```toml
[build-system]
requires = ["whey", "whey-mixin", "Babel"]
build-backend = "whey"

[tool.whey.mixin]
hooks = [
  "build_hooks:build_messages"
]

[tool.whey.mixin.exe]
class = "my_builders:ExeBuilder"
hooks = []
```

Both hooks and class are [entry points](https://packaging.python.org/en/latest/specifications/entry-points/) which specify the function or class to load, respectively. For use with this system, they will generally be relative to the root directory of your project. However, that's not required, and they can be from other modules as well.

Hooks specified in `tool.whey.mixin` run before build-specific hooks. They will run for every mixin builder, so if you don't want that, you will have to put the hook in individual build configs.

If a module defines its own named entry point that you wish to add hooks to, you may use the key `entry-point` instead of `class` to specify the entry point name.
