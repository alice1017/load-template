# load-template

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

## :page_facing_up: Overview

The **load-template** create a file from the **template** with the **variables**.
You can create templates as freely if you save it :open_file_folder: `~/.templates/`.

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
* *-D*, *--dev* - Run development mode.

### template variable

You can set some variables to the template as follows:

```
<h1>Hello, {name}</h1>
```

when use this variable:

```
$ load-template template hello.html name=Alice
```

## :inbox_tray: Installation

```
$ git clone git@github.com:alice1017/load-template.git
$ cd load-template
$ python setup.py build install
```

You need to clone this repository for installation, Because the
load-template copies the default templates to `~/.templates/` directory.


