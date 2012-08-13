#!/bin/bash

# Get script directory: http://stackoverflow.com/a/246128/756056
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# kill everything which runs with virtualenv's python
kill $(ps aux | grep "${DIR}/bin/python" | grep -v grep | awk '{print $2}')