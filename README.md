# load-template

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

[![Build Status](https://travis-ci.org/alice1017/load-template.svg?branch=master)](https://travis-ci.org/alice1017/load-template)
[![Coverage Status](https://coveralls.io/repos/github/alice1017/load-template/badge.svg)](https://coveralls.io/github/alice1017/load-template)
![Python 2.7 only](https://img.shields.io/badge/python-2.7-blue.svg)

* [:page_facing_up: Overview](#page_facing_up-overview)
* [:wrench: Usage](#wrench-usage)
* [:inbox_tray: Installation](#inbox_tray-installation)
* [:eyes: Contribution](#eyes-contribution)
* [CHANGELOG](#changelog)

## :page_facing_up: Overview

The **load-template** create a file from the **template** with the **variables**,
and **edit** the file in your **editor**.

You can create templates as freely if you save it :open_file_folder: `~/.templates/`.

If you want to add new default template, please send pull request. :+1:

## :wrench: Usage

### basic

```
$ load-template [template] [file] [variables [variables ...]]
```

### positional arguments

* ***template*** - The template name. You can show all templates by `--list`.
* ***file*** - The file name to create.
* ***variables*** - The template variables formatted `key=value`.

### optional arguments

* *-l*, *--list* - Display the all template list.
* *-c*, *--contents* - Display contents of the template.
* *-s*, *--sync* - Sync the default template to local template. Before using this feature, you have to do `git pull`.
* *-D*, *--dev* - Run development mode.

### template variable

You can set some **variables** to the template as follows:

```html
<h1>Hello, {name}</h1>
```

when use this variable:

```
$ load-template template hello.html name=Alice
```

rendered:

```html
<h1>Hello, Alice</h1>
```

## :inbox_tray: Installation

```
$ git clone git@github.com:alice1017/load-template.git
$ cd load-template
$ python setup.py build install
```

You **need to clone this repository** for installation, Because the
load-template **copies** the default templates to `~/.templates/` directory.

## :eyes: Contribution

1. Forks on [Github](https://github.com/alice1017/load-template)
2. Find a bug? Add new default template? Send a pull request to get it merged and published.

## CHANGELOG

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)

### [1.0.0] - 2018/4/16

#### Added new feature

* Added `--contents` argument to display template contents. Fixed [#2]
* Added **edit** feature. Fixed [#3]
* Added `--sync` argument to sync default template and local template. Fixed [#1]

#### Added new template

* Added `templates/readme-py` template.
* Added `templates/python-argparser` template.

#### Changed

* Changed a template name: `mit_license` to `mit-license`

#### Other

* Use [**travis-ci**](https://travis-ci.org/alice1017/load-template).
* Use [**coverall**](https://coveralls.io/github/alice1017/load-template).

### [1.0.0b1] - 2018/3/28

A Beta Version Release.

[1.0.0b1]: https://github.com/alice1017/load-template/compare/a2f5136...1.0.0b1
[1.0.0]: https://github.com/alice1017/load-template/compare/1.0.0b1...1.0.0
[#1]: https://github.com/alice1017/load-template/issues/1
[#2]: https://github.com/alice1017/load-template/issues/2
[#3]: https://github.com/alice1017/load-template/issues/3
