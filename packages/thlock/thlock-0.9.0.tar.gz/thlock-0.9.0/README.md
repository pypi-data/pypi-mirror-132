[![Build][build-image]]()
[![Stable Version][stable-image]][stable-url]
[![Coverage][coverage-image]]()
[![License][bsd3-image]][bsd3-url]

# thlock

## Overview
TangledHub library for etcd_lock with a focus on asynchronous functions

## Licencing
thlock is licensed under the BSD license. Check the [LICENSE](https://opensource.org/licenses/BSD-3-Clause) for details

---

## Installation
```bash
pip install thlock
```

## Testing
```bash
docker-compose build thlock-test ; docker-compose run --rm thlock-test
```

## Building
```bash
docker-compose build thlock-build ; docker-compose run --rm thlock-build
```

## Publish
```bash
docker-compose build thcrypto-lock ; docker-compose run --rm -e PYPI_USERNAME=__token__ -e PYPI_PASSWORD=__SECRET__ thlock-publish
```

---

## Usage

### setup

Create instance of EtcdLock

```python

HOST = 'etcd-test'
PORT = 2379

# create instance of EtcdLock
lock = EtcdLock(host=HOST, port=PORT, name='lock-0')

```


### Acquire lock

```python

HOST = 'etcd-test'
PORT = 2379

# create instance of EtcdLock
lock = EtcdLock(host=HOST, port=PORT, name='lock-0')

# acquire lock
await lock.acquire()

```


<!-- Links -->

<!-- Badges -->

[bsd3-image]: https://img.shields.io/badge/License-BSD_3--Clause-blue.svg
[bsd3-url]: https://opensource.org/licenses/BSD-3-Clause
[build-image]: https://img.shields.io/badge/build-success-brightgreen
[coverage-image]: https://img.shields.io/badge/Coverage-100%25-green
[stable-image]: https://img.shields.io/pypi/v/thlock?label=stable
[stable-url]: https://pypi.org/project/thlock/

