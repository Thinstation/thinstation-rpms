This repository contains patches and GitHub Actions that produce RPMs patched
or built specifically for thinstation-ng.

Published repository layout:

    https://thinstation.github.io/thinstation-rpms/<thinstation-version>/<arch>/

For ThinStation 7.4 the builder publishes both:

    7.4/x86_64/
    7.4/aarch64/

The 7.4 repositories contain the ThinStation BusyBox variants and gtkdialog.
The gtkdialog RPM is built from the pinned upstream source revision in
specs/gtkdialog.spec.

Older ThinStation release repositories remain x86_64-only.
