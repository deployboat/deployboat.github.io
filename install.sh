#!/usr/bin/env bash
# Short address for the Deploy Boat installer:
#   curl -fsSL deployboat.github.io/install.sh | sudo bash
#   curl -fsSL deployboat.github.io/install.sh | sudo bash -s -- --domain example.com
#   curl -fsSL deployboat.github.io/install.sh | sudo bash -s -- --version v0.5.0
#
# It runs the real installer from the latest release (attached to every GitHub Release),
# so even the installer itself is a released, tested version.
# With --edge, or if there are no releases yet, it uses the installer on main instead.
set -euo pipefail

RELEASE=https://github.com/deployboat/deployboat/releases/latest/download/install.sh
MAIN=https://raw.githubusercontent.com/deployboat/deployboat/main/install.sh

case " $* " in
  *" --edge "*) script="$(curl -fsSL "$MAIN")" ;;
  *) script="$(curl -fsSL "$RELEASE" 2>/dev/null || curl -fsSL "$MAIN")" ;;
esac
bash -s -- "$@" <<<"$script"
