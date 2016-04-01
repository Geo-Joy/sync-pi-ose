[![Build Status](https://travis-ci.org/wireload/sync-ose.svg?branch=master)](https://travis-ci.org/wireload/sync-ose)
[![Coverage Status](https://coveralls.io/repos/wireload/sync-ose/badge.svg?branch=master&service=github)](https://coveralls.io/github/wireload/sync-ose?branch=master)

# SYNC OSE - Digital Signage for the Raspberry Pi

To learn more about SYNC, please visit the official website at [SYNCApp.com](http://www.syncapp.com). On the official site, you'll find the complete installation instructions, along with a live-demo of SYNC.

## Dockerized Development Environment

To simplify development of the server module of SYNC OSE, we've created a Docker container. This is intended to run on your local machine with the SYNC OSE repository mounted as a volume.

Assuming you're in the source code repository, simply run:

```
$ docker run --rm -ti \
  -p 8080:8080 \
  -v $(pwd):/home/pi/sync \
  wireload/sync-ose-server
```

## Disk Image Changelog

### 2015-02-25

 * Adds support for Raspberry Pi B+ V2.
 * Upgrades kernel and kernel modules.
 * Brings system packages up to date.
 * Various bug fixes.

### 2014-11-03

 * Adds a setting for time display in 24 or 12 hour formats.
 * System updates (including Bash and OpenSSL).
 * Solves a UTF8 bug ([#226](https://github.com/wireload/sync-ose/issues/226)).
 * Various bug fixes.

### 2014-08-13

 * Adds support for Raspberry Pi Model B+.
 * Improves handling in `viewer.py` where the splash page is being displayed before `server.py` has been fully loaded.
 * Pulls in APT updates from SYNC's APT repository.
 * Other bug fixes up to commit 1946e252471fcf34c27903970fbde601189d65a5.

### 2014-07-17

 * Fixes issue with load screen failing to connect.
 * Adds support for video feeds ([#210](https://github.com/wireload/sync-ose/issues/210)).
 * Resolves issue with assets not being added ([#209](https://github.com/wireload/sync-ose/issues/209)).
 * Resolves issue with assets not moving to active properly ([#201](https://github.com/wireload/sync-ose/issues/201)).
 * Pulls in APT updates from SYNC's APT repository.

### 2014-01-11

 * Upgrade kernel (3.10.25+) and firmware. Tracked in [this](https://github.com/wireload/rpi-firmware) fork.
 * Change and use SYNC's APT repository (apt.syncapp.com).
 * `apt-get upgrade` to the SYNC APT repository.
 * Update SYNC to latest version.
 * The disk image is available at [SYNCApp.com](http://www.syncapp.com).

## Running the Unit Tests

    nosetests --with-doctest

