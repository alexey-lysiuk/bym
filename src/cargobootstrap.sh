#!/bin/sh

set -o errexit

if [ -z "$1" ]; then
	echo "No installation path specified"
	exit 1
fi

CARGO_URL=https://static.rust-lang.org/dist/2019-01-17/cargo-0.33.0-x86_64-apple-darwin.tar.gz
CARGO_FILENAME=$(basename ${CARGO_URL})
CARGO_DIRNAME=${CARGO_FILENAME%.tar.gz}

curl -LO "${CARGO_URL}"

shasum -a 256 "${CARGO_FILENAME}" > __actual_sum__
echo "25cf75479da383d2307e1d6204e915f628ec3f1c185b124f57839cfd622f54b1  ${CARGO_FILENAME}" > __expected_sum__
diff -q __actual_sum__ __expected_sum__ > /dev/null

tar -xf "${CARGO_FILENAME}"
"${CARGO_DIRNAME}/install.sh" --prefix="`pwd`/__cargobootstrap__"

# Quick and dirty workaround for potential libssh2 conflict
if [ -f "$1/include/libssh2.h" ]; then
	mv "$1/include/libssh2.h" "$1/include/libssh2.h.cargoboostrap"
fi

__cargobootstrap__/bin/cargo install --root "$1" --path .

if [ -f "$1/include/libssh2.h.cargoboostrap" ]; then
	mv "$1/include/libssh2.h.cargoboostrap" "$1/include/libssh2.h"
fi
