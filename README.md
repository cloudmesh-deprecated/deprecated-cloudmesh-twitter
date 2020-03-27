# Documentation

## Instalation

* Make sure you sue python 3.8.2
* Makes usre you have a venve in ~/ENV3

```bash
pip install cloudmesh-installer
cloudmesh-installer get twitter
```

## Usage

```bash
$ cms help twitter
```

## Manual Page

```
  Usage:
    cms twitter register [REGISTER]
    cms twitter stream start [--file=FILE]
                             [--attributes=ATTRIBUTES]
                             [--filter=FILTER]

  Arguments:
    REGISTER  a file name with the registration information
              [default: ~/.cloudmesh/twitter.json]
    FILE      The file to which the stream is redirected.
              By default this is stdout
              [default: stdout]

  Options:
      -f      specify the file

  Descriptions:

    filter is not realy that imporatnt, attributes are

    cms twitter register [FILE]

      Registers the titter API with data stored in the file.
      TODO: findout which data is used and whcih format it has.
            Use the format that twitter offers

    cms twitter stream start [--file=FILE]
                             [--attributes=ATTRIBUTES]
                             [--filter=FILTER]

       Starts the twitter stream and redirects it to the given file. If
       stdout is specified it just prints it. Twitter returns a number
       of attributs in a tweet. You can specify a comma separated list
       of attributes that are stored instead of all attributes. If you
       do not specify attributes, all attributes will be returned.

       The filter is currently unimportant, but we want to be able to
       identify in future just some tweets that match this pattern.

```