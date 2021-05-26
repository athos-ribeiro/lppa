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
ppa create [all|arch, ...]
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

## Development

Read the Makefile.

Run `make devel` to set the development environment up (a python virtual
environment is recommended).

Run `make check` to run the test suite and ensure the development environment
is up to date.
