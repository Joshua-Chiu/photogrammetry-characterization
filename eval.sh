#!/usr/bin/env bash
set -e

handle_error() {
    echo "An error occurred on line $1"
    exit 1
}

trap 'handle_error $LINENO' ERR

HEADER='\033[95m'
OKBLUE='\033[94m'
OKCYAN='\033[96m'
OKGREEN='\033[92m'
WARNING='\033[93m'
FAIL='\033[91m'
ENDC='\033[0m'
BOLD='\033[1m'
UNDERLINE='\033[4m'

echo -e "${HEADER}***** Running all python scripts *****${ENDC}"

/usr/bin/python3 ~/Documents/photogrammetry-characterization/compare-hausdorff.py objects/groundtruth.obj $1
/usr/bin/python3 ~/Documents/photogrammetry-characterization/compare-mae-mse.py objects/groundtruth.obj $1

echo -e "${OKGREEN}***** Exit *****${ENDC}"