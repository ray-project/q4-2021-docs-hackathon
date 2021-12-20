# 2021 Q4 Ray documentations hackathon: Proposal for new Ray documentation

# Instructions

To install all dependencies with Python 3, run

```shell
pip install -r requirements.txt
```

To build and run the documentation then simply run

```shell
mkdocs build
```

# About

- This proof-of-concept is built using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- Changes merged into the `main` branch will be automatically build and published at: https://ray-project.github.io/q4-2021-docs-hackathon
- Using [mike](https://github.com/jimporter/mike) to manage versioning
  - Note that the Github CI is using a fake version (i.e. v0.3). It will always deploy changes to the 0.3 version just for demo purposes.
- Code snippets are include using [`mdx_include`](https://github.com/neurobin/mdx_include)
- Jupyter notebooks get rendered on the fly with [`mkdocs-jupyter`](https://github.com/danielfrg/mkdocs-jupyter)
- API references are generated with [`mkdocstrings`](https://github.com/mkdocstrings/mkdocstrings)
