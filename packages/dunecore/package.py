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
#     spack install dunecore
#
# You can edit this file again by typing:
#
#     spack edit dunecore
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Dunecore(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/DUNE/dunecore/archive/refs/tags/v09_81_00d00.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("09_81_00d00", sha256="4dd8f63fd791167bc55c5fba28f0a9310c2339c0cc3c70bd15e510d36d0ff972")

    # FIXME: Add dependencies if required.
    depends_on("dunepdlegacy")
    depends_on("dunedaqdataformats")
    depends_on("dunedetdataformats")
    depends_on("duneutil")
    depends_on("larsoft")
    depends_on("highfive")
    depends_on("cetmodules", type="build")
    depends_on("cetbuildtools", type="build")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
