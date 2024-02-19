#!/bin/bash
#
# Copyright 2022 Intel Corporation
# SPDX-License-Identifier: MIT
#

#FIXME: 맥 환경 테스트를 위한 수정 
ARCH=macos-arm64
VERSION=0.21.10

echo "Download sqlean extensions for arch=${ARCH}"
rm -f sqlean-${ARCH}.zip
wget https://github.com/nalgeon/sqlean/releases/download/${VERSION}/sqlean-${ARCH}.zip
unzip -p sqlean-${ARCH}.zip stats.dylib > stats.so
rm -f sqlean-${ARCH}.zip
