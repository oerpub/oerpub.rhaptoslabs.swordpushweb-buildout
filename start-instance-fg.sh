#!/bin/bash

# Get script directory: http://stackoverflow.com/a/246128/756056
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Start as deamon service
${DIR}/bin/python ${DIR}/bin/paster serve ${DIR}/src/oerpub.rhaptoslabs.swordpushweb/oerpub/rhaptoslabs/production.ini
