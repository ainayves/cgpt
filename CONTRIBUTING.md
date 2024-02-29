# Contributor Guide

Thank you for your interest in improving this project.
This project is open-source under the [MIT license] and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

Here is a list of important resources for contributors:

- [Source Code]
- [Documentation]
- [Issue Tracker]
- [Code of Conduct]

[mit license]: https://opensource.org/licenses/MIT
[source code]: https://github.com/ainayves/cgpt
[documentation]: https://cgpt.readthedocs.io/
[issue tracker]: https://github.com/ainayves/cgpt/issues

## How to request a feature or report a bug ?

Request features on the [Issue Tracker].

## How to set up your development environment

You need Python 3.7+ and the following tools:

- [Poetry]
- [Nox]
- [nox-poetry]

Install the package with development requirements:

```console
$ poetry install
```

You can now run an interactive Python session,
or the command-line interface:

```console
$ poetry run python
$ poetry run cgpt
```

[poetry]: https://python-poetry.org/
[nox]: https://nox.thea.codes/
[nox-poetry]: https://nox-poetry.readthedocs.io/

## How to test the project

Run the full test suite:

```console
$ nox
```
## Use Devbox 

Devbox is a powerful tool that lets you easily create isolated shells for development.

You need to install [Devbox](https://www.jetpack.io/devbox/docs/installing_devbox/) if you do not have it yet.

Then , run this command in the root directory of the project to test the tool :

```
$ devbox run start
```

Run this to test the LAN mode :

```
$ devbox run lan
```

Run this to test api_key modification :

```
$ devbox run apikey
```

[pull request]: https://github.com/ainayves/cgpt/pulls

<!-- github-only -->

[code of conduct]: CODE_OF_CONDUCT.md
