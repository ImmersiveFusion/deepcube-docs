# DeepCube Documentation

This repository contains the source for the [DeepCube](https://docs.immersivefusion.com/) (3D, Web, Studio) and Tessa documentation site, built with [MkDocs](https://www.mkdocs.org/) and the Material theme.

📖 **Published site:** https://docs.immersivefusion.com/

This repo is where corrections and additions to the docs are made, changes here are what eventually ship to the published site above.

## Structure

- `docs/` — the actual documentation pages (Markdown source)
- `overrides/` — theme customizations for the Material theme
- `templates/` — page/layout templates used across the docs

## Previewing locally

`.\serve.ps1` runs a local preview using `mkdocs.dev.yml`, a dev-specific config that skips slower plugins (like git revision dates) for faster rebuilds while you write:

```powershell
.\serve.ps1
```

This is equivalent to running `envprep.ps1` followed by `python -m mkdocs serve -f mkdocs.dev.yml` directly.

See the build instructions below for environment setup.

# Getting started

Follow the steps at https://www.mkdocs.org/

## Installing Python
1. Determine if `python` needs to be installed, follow instructions on https://www.python.org/downloads/ Make sure to select add to PATH

```
$ python --version
Python 3.12.4
```

## Installing Mkdocs and plugins

```ps
& envprep.ps1
```

## Run 
```ps
powershell .\serve.ps1
```

Look at the serve output for the local URL for the docs.


## Use rich elements
https://squidfunk.github.io/mkdocs-material/

## Publish with from folder where the yaml file is
```
mkdocs build
```
