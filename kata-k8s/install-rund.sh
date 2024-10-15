#!/bin/bash

set -x

SHIM_NAME="containerd-shim-rund-v2"
GUEST_IMG_NAME="kata-containers-rund.img"
SHARED_VOLUME="/vagrant"

if [ ! -f "$SHARED_VOLUME/$SHIM_NAME" ]; then
  echo "$SHIM_NAME not found"
  exit 1
fi

if [ ! -f "$SHARED_VOLUME/$GUEST_IMG_NAME" ]; then
  echo "$GUEST_IMG_NAME not found"
  exit 1
fi

cp -f "$SHARED_VOLUME/$SHIM_NAME" "/usr/local/bin/$SHIM_NAME"
cp -f "$SHARED_VOLUME/$GUEST_IMG_NAME" "/root/$GUEST_IMG_NAME"
