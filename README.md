# Docker images

[![Build Status](https://travis-ci.org/NYAG/dockers.svg?branch=master)](https://travis-ci.org/NYAG/dockers)

This repository contains Dockerfiles intended for use by the
Department of Research and Analytics at the
[New York State Office of the Attorney General][nyag].

## dumpling

[dumpling][dumpling] is our Docker image containing common
packages and tools for a consistent data science environment,
including Python 3, Pandas, Jupyter, Git, and [oaglib].

When contributing changes, please add tests to
[`bin/dumpling-test`](bin/dumpling-test).

[nyag]: https://ag.ny.gov/
[dumpling]: https://hub.docker.com/r/nyag/dumpling/
[oaglib]: https://github.com/NYAG/oaglib
