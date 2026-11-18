#!/usr/bin/env bash
# Short address for the Deploy Boat installer:
#   curl -fsSL deployboat.github.io/install.sh | sudo bash
# It runs the real installer, always the latest version from the main repo:
#   https://github.com/deployboat/deployboat/blob/main/install.sh
set -euo pipefail
curl -fsSL https://raw.githubusercontent.com/deployboat/deployboat/main/install.sh | bash
