# Qubes security pack (qubes-secpack)

The [Qubes security pack (qubes-secpack)](https://doc.qubes-os.org/en/latest/project-security/security-pack.html) is a git repository containing security-related information about the Qubes OS Project. It includes the following:

 - Qubes PGP keys (`keys/`)
 - Qubes security bulletins (`QSBs/`)
 - Qubes canaries (`canaries/`)
 - Qubes fund information (`fund/`)
 - Qubes ISO digests (`digests/`)

The files contained in this repository can be [authenticated](https://doc.qubes-os.org/en/latest/project-security/security-pack.html#how-to-obtain-and-authenticate) in two ways:

 - By verifying the git commit tags (`git tag -v`)
 - By verifying the detached PGP signatures, which are provided for the majority of files included here (e.g., individual QSBs, canaries, and other announcements)

All the keys used by the Qubes OS Project itself, including the keys used to sign files and commits in this repository (but excluding keys owned by individual people), are ultimately signed by the Qubes Master Signing Key (QMSK). Even though the QMSK is included in this repo, you should make sure to [obtain the QMSK fingerprint from multiple independent sources in several different ways](https://doc.qubes-os.org/en/latest/project-security/verifying-signatures.html#how-to-import-and-authenticate-the-qubes-master-signing-key), as a fake Qubes security pack would contain a fake QMSK.
