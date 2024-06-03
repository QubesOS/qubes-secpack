Keys to sign Qubes OS, directory contains:
- `master-key` - the Qubes Master Signing Key used to sign other keys
- `release-keys` - keys used to sign official installation images
- `core-dev` - keys used to sign source code (version and release tags)
- `security-team` - keys used to sign tags in this (qubes-secpack)
  repository, Qubes Canaries and Qubes Security Bulletins
- `template-keys` - keys used to sign packages for templates (official
  and community); those keys are not signed with the master key
  (except the one for Fedora packages, which is the same as for dom0
  packages and installation images); the templates-* keys are
  used to sign whole templates;
  note the R4.0 and R4.1 uses the same set of keys
- `doc-signing` - keys used to sign documentation and website
  repositories
