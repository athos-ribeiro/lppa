# Python PPA

Command line tool to create Launchpad PPAs and push deb source packages to them

## Installation

```
pip install .
```

## Usage

ppa ships a `ppa` command line application to interact with Launchpad PPAs.
Run

```
ppa --help
```

for additional information.

### Create a new PPA

To create a new PPA, run

```
ppa create PPA_NAME [all|arch, ...]
```

where arch is a Launchpad processor (you can pass multiple architectures here)
or `all` to enable all available architectures.

The currently available Launchpad processors are

- amd64
- arm64
- s390x
- ppc64el
- armhf
- armel
- i386
- powerpc

### Delete an existing PPA

```
ppa delete PPA_NAME
```

### List user's PPAs

```
ppa list
```

This will print a list with the names of the user's available PPAs

### Fetch PPA information

Often, you may want to retrieve an URL for a PPA packages page or quickly fetch
a dput command to upload packages to a PPA. That can be achieved through the
`info` command.

```
ppa info PPA_NAME
```

Moreover, passing the `-v` option to the info command will also display the
architectures for which the PPA can build packages.

## Development

Read the Makefile.

Run `make devel` to set the development environment up (a python virtual
environment is recommended).

Run `make check` to run the test suite and ensure the development environment
is up to date.
