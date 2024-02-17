# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install duneutil
#
# You can edit this file again by typing:
#
#     spack edit duneutil
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Duneutil(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/DUNE/duneutil/archive/refs/tags/v09_81_00d00.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("09_81_00d00", sha256="3cd857e366c7ecf1648f0f7aa76c2821ba25fe8b8d702ff47e2d7291d006a3bf")

    # FIXME: Add dependencies if required.
    depends_on("art-root-io")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
