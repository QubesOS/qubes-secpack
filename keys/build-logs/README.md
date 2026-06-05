Keys in this directory are used to sign build logs. Separate keys are
used depending on the build artifact category:

- `packages-release.asc` - release packages for dom0 and officially supported templates (Fedora, Debian), and for the official template builds themselves too
- `packages-community.asc` - release packages for community supported templates (when built on official infrastructure) - Archlinux, Ubuntu
- `templates-community.asc` - community template builds
- `packages-devel.asc` - devel version packages for testing purpose

