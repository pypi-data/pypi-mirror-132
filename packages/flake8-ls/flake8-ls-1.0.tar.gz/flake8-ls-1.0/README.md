# flake8-ls: super fast mypy language server

It leverages mypy.flake8_server instead of the slow cli interface.

First run takes same time as mypy cli, but next are super fast as
mypy.flake8_server only reload the changed file.

It supports diagnostics only.

## Status

On works on Open and Save for now

The on Change could be implemented if the mypy FineGrainedBuildManager uses
BuildSource of the flake8_server instead of always reread file from disk...

## Install

```shell
$ pip install --user flake8-ls
```

## vim-lspconfig

```lua
lua << EOF
require("lspconfig.configs")["flake8ls"] = {
    default_config = {
        cmd = { 'flake8-ls' },
        filetypes = { 'python' },
        root_dir = lspconfig.util.root_pattern('pyproject.toml', 'setup.py', 'setup.cfg', 'requirements.txt', 'Pipfile'),
        single_file_support = true,
    },
}
require("lspconfip").flake8ls.setup({})
EOF
```
