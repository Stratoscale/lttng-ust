#!/bin/sh

rpmbuild -ba /root/rpmbuild/SPECS/lttng-ust.spec

cp /root/rpmbuild/RPMS/x86_64/*.rpm /output_rpms
