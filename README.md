Qubes Security Pack
===================

This git repository is a central place for all security-related information
about the Qubes OS Project. It includes the following:

 * Qubes PGP keys (`keys/`)
 * Qubes Security Bulletins (`QSBs/`)
 * Qubes warrant canaries (`canaries/`)
 * Qubes Bitcoin fund information (`fund/`)
 * Qubes ISO digests (`digests/`)

The files contained in this repository can be verified in two ways:

 * By verifying the git commit tags (`git tag -v`)
 * By verifying the detached PGP signatures, which are provided for the majority
   of files included here (e.g. individual QSBs, canaries, and other
   announcements)

All the keys used by the Qubes OS Project, including the keys used to
sign files and commits in this repository, are signed by the Qubes Master
Signing Key. Even though this key is also included in this repo, you should
make sure to obtain the master key fingerprint via some other
channel, as you can be sure that if you were getting a falsified Qubes
Security Pack it would contain a falsified master key as well.

For more information about the Qubes Security Pack, including its history and
rationale, and for detailed instructions for verifying its contents, please see
its [documentation page](https://www.qubes-os.org/doc/security-pack/).

