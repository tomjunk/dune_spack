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
#     spack install duneana
#
# You can edit this file again by typing:
#
#     spack edit duneana
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Duneana(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/DUNE/duneana/archive/refs/tags/v09_81_00d00.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("09_81_00d00", sha256="8c1fc6758232a9b4ba7a39924ea372d8e2698404bf4778c9b209a35d8888dcf4")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch('v09_81_00d00.patch', when='@09_81_00d00')

    # FIXME: Add dependencies if required.
    depends_on("duneanaobj")
    depends_on("duneopdet")
    depends_on("dunereco")
    depends_on("nufinder")
    depends_on("larfinder")
    #depends_on("py-tensorflow")
    #depends_on("python")
    depends_on("systematicstools")
    depends_on("cetmodules", type="build")
    depends_on("cmake", type="build")

    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("CMAKE_MODULE_PATH", "%s/Modules;%s/Modules" %
                       (self.spec['nufinder'].prefix, self.spec['larfinder'].prefix))
        ] 
        return args

    #def setup_build_environment(self, spack_env):
    #    spack_env.set("TENSORFLOW_DIR", str(self.spec["py-tensorflow"].prefix.lib))
    #    spack_env.set(
    #        "TENSORFLOW_INC",
    #        str(
    #            join_path(
    #                self.spec["py-tensorflow"].prefix.lib,
    #                "python%s/site-packages/tensorflow/include"
    #                % self.spec["python"].version.up_to(2),
    #            )
    #        ),
    #    )
