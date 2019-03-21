#!/usr/bin/with-contenv bash

PUID=${PUID:-15000}
PGID=${PGID:-15000}

# - Documents created by www-data user, not 15000 like all other containers.
# change mayan userid
groupmod -g "$PGID" mayan
usermod -u "$PUID" mayan

chown -R mayan:mayan "$PROJECT_INSTALL_DIR"

# fix for http://mayan-edms.1003.x6.nabble.com/Mayan-EDMS-2001-docker-local-py-settings-import-error-td5002909.html
# - Startup /var/lib/mayan/settings folder needs to exist for local.py settings to be created
mkdir -p /var/lib/mayan/settings

chown -R mayan:mayan /var/lib/mayan


# - FUSE index/volume mount - https://docs.mayan-edms.com/chapters/indexes.html?highlight=fuse
# - Set Admin password - https://github.com/mayan-edms/mayan-edms/issues/259
# - Set Watch Folder -
