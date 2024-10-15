#!/bin/bash

# This script DOES NOT install runD shim, config and image.
# This script MUST be run as root.
# 
# Steps:
# 1. Patch containerd config with rund config.
# 2. Install a runtimeclass for runD on K8s.

set -x

if [ "$UID" -ne 0 ]; then
    echo "This script must be run as root."
    exit 1
fi

export no_proxy="$no_proxy,10.0.0.0/8,192.168.0.0/16" \
  && export NO_PROXY=${no_proxy} \
  && echo "no_proxy => $no_proxy"

CONTAINERD_CONFIG_PATH="/etc/containerd/config.toml"
if [ ! -f "$CONTAINERD_CONFIG_PATH" ] || [ ! -r "$CONTAINERD_CONFIG_PATH" ] && [ ! -w "$CONTAINERD_CONFIG_PATH" ]; then
  exit 1
fi

RUND_PATTERN="containerd.runtimes.rund"
if [ -z "$(grep "$RUND_PATTERN" $CONTAINERD_CONFIG_PATH)" ]; then
  cp $CONTAINERD_CONFIG_PATH "$CONTAINERD_CONFIG_PATH.bak"
  sed -i '/\[plugins\."io\.containerd\.grpc\.v1\.cri"\.containerd\.runtimes\]/a\
        \
        [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.rund]\
          pod_annotations = ["io.katacontainers.*"]\
          privileged_without_host_devices = true\
          privileged_without_host_devices_all_devices_allowed = true' $CONTAINERD_CONFIG_PATH
  if [ -z "$(grep "$RUND_PATTERN" $CONTAINERD_CONFIG_PATH)" ]; then
    mv "$CONTAINERD_CONFIG_PATH.bak" $CONTAINERD_CONFIG_PATH
    echo "failed to patch containerd config."
    exit 1
  fi
  systemctl daemon-reload
  systemctl restart containerd
fi

if [ -z "$(kubectl get runtimeclass | grep rund)" ]; then
  cat > /tmp/rund-runtimeclass.yaml <<EOF
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: rund 
handler: rund
EOF
  kubectl apply -f /tmp/rund-runtimeclass.yaml
fi
