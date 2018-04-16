# load-template

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

[![Build Status](https://travis-ci.org/alice1017/load-template.svg?branch=master)](https://travis-ci.org/alice1017/load-template)
[![Coverage Status](https://coveralls.io/repos/github/alice1017/load-template/badge.svg)](https://coveralls.io/github/alice1017/load-template)
![Python 2.7 only](https://img.shields.io/badge/python-2.7-blue.svg)

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
