#!/bin/bash

set -eu

DSP8010_VERSION='2025.2'
SWORDFISH_VERSION='1.2.8'

DSP8010_FILE="DSP8010_${DSP8010_VERSION}.zip"
DSP8010_URL="https://www.dmtf.org/sites/default/files/standards/documents/${DSP8010_FILE}"

SWORDFISH_FILE="Swordfish_v${SWORDFISH_VERSION}.zip"
SWORDFISH_URL="https://www.snia.org/sites/default/files/technical-work/swordfish/release/v${SWORDFISH_VERSION}/zip/${SWORDFISH_FILE}"

APP_ROOT="$(dirname "$0")/.."
APP_ROOT=$(cd "$APP_ROOT"; pwd)
OUTPUT_DIR="${APP_ROOT}/src/redfish_service"

WORK_DIR=$(mktemp -d)
trap 'rm -rf ${WORK_DIR}' EXIT

pushd "${WORK_DIR}"

# redfish
mkdir ./redfish
mkdir -p ./spec/redfish
curl -sSLO "${DSP8010_URL}"
unzip "${DSP8010_FILE}" -d ./redfish
mv ./redfish/*/json-schema/* ./spec/redfish

# swordfish
mkdir -p ./swordfish/schemas
mkdir -p ./spec/swordfish
curl -sSLO "${SWORDFISH_URL}"
unzip "${SWORDFISH_FILE}" -d ./swordfish
unzip "swordfish/Swordfish_v${SWORDFISH_VERSION}_Schema.zip" -d ./swordfish/schemas
mv ./swordfish/schemas/json-schema/* ./spec/swordfish

# Generating model.
rm -rf "${OUTPUT_DIR}"/model/*
rm -rf "${OUTPUT_DIR}"/router/*
uv run "${APP_ROOT}"/tools/gen/main.py ./spec/redfish ./spec/swordfish "${OUTPUT_DIR}"

# Format.
pushd "${APP_ROOT}"
uv run ruff format && uv run ruff check --fix
uv run ruff format && uv run ruff check --fix
uv run ruff format && uv run ruff check --fix
