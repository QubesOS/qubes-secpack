This repository contains various PGP keys used throughout the Qubes OS Project.

- `master-key/` contains the [Qubes Master Signing Key (QMSK)](https://www.qubes-os.org/security/verifying-signatures/#how-to-import-and-authenticate-the-qubes-master-signing-key), which is used to sign certain other security-critical keys.

- `release-keys/` contains [release signing keys (RSKs)](https://www.qubes-os.org/security/verifying-signatures/#how-to-import-and-authenticate-release-signing-keys), which are used to sign Qubes OS installation images (ISOs) and dom0 packages.

- `core-devs/` contains keys belonging to Qubes core developers. These keys are used to sign Git version and release tags in source code repositories.

- `security-team/` contains keys belonging to the [Qubes security team (QST](https://www.qubes-os.org/security/#qubes-security-team). These keys are used to sign [Qubes security bulletins (QSBs)](https://www.qubes-os.org/security/qsb/), [Qubes canaries](https://www.qubes-os.org/security/canary/), and the [Qubes security pack (qubes-secpack)](https://www.qubes-os.org/security/pack/).

- `template-keys/` contains keys used to sign [templates](https://www.qubes-os.org/doc/templates/) and their packages. These keys are not signed by the QMSK (except for the Fedora package signing key, since it is also used for dom0 packages and ISOs). Keys containing `templates` in the name are used to sign whole templates. Note that the Qubes OS 4.0 and 4.1 releases use the same set of keys.

- `doc-signing/` contains keys belonging to Qubes documentation and website editors.
