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
    url = "https://github.com/DUNE/dunecore/archive/refs/tags/v09_89_01d01.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("09_92_00d00", sha256="37edf3afd3be02cbd64adef1ab1c5c9c7e275d7ffcee44ffce2172451f94dbcd")
    version("09_89_01d01", sha256="cf61a68d0810103bd45a1133a969378817caf2e09be87ebcaea718ac4bd09060")
    version("09_81_00d00", sha256="4dd8f63fd791167bc55c5fba28f0a9310c2339c0cc3c70bd15e510d36d0ff972")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch('v09_81_00d00.patch', when='@09_81_00d00')

    depends_on("boost")
    depends_on("geant4")
    depends_on("root")
    depends_on("eigen")
    depends_on("art")
    depends_on("art-root-io")
    depends_on("artdaq-core")
    depends_on("trace")
    depends_on("canvas")
    depends_on("canvas-root-io")
    depends_on("cetlib-except")
    depends_on("cetlib")
    depends_on("clhep")
    depends_on("fhicl-cpp")
    depends_on("nufinder")
    depends_on("genie")
    depends_on("hep-concurrency")
    depends_on("ifdh-art")
    depends_on("ifdhc")
    depends_on("dunepdlegacy")
    depends_on("duneutil")
    depends_on("larsoft")
    depends_on("larana")
    depends_on("larcore")
    depends_on("larcorealg")
    depends_on("larcoreobj")
    depends_on("lardata")
    depends_on("lardataalg")
    depends_on("lardataobj")
    depends_on("larevt")
    depends_on("larpandora")
    depends_on("larreco")
    depends_on("larsim")
    depends_on("messagefacility")
    depends_on("nuevdb")
    depends_on("nug4")
    depends_on("nugen")
    depends_on("nurandom")
    depends_on("nusimdata")
    depends_on("nutools")
    depends_on("pandora")
    depends_on("dunedaqdataformats")
    depends_on("dunedetdataformats")
    depends_on("postgresql")
    depends_on("fftw")
    depends_on("sqlite")
    depends_on("nlohmann-json")
    depends_on("highfive")
    depends_on("hdf5")
    depends_on("cetmodules", type="build")
    depends_on("cmake", type="build")

    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("CMAKE_MODULE_PATH", "%s/Modules" % self.spec['nufinder'].prefix)
        ] 
        return args

    def setup_build_environment(self, spack_env):
        spack_env.set("LD_LIBRARY_PATH", "%s/root" % self.spec["root"].prefix.lib)

    def setup_run_environment(self, run_env):
        run_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        run_env.append_path("FHICL_FILE_PATH", "{0}/fcl".format(self.prefix))
        run_env.append_path("FW_SEARCH_PATH", "{0}/gdml".format(self.prefix))

    def setup_dependent_run_environment(self, run_env, dspec):
        run_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        run_env.append_path("FHICL_FILE_PATH", "{0}/fcl".format(self.prefix))
        run_env.append_path("FW_SEARCH_PATH", "{0}/gdml".format(self.prefix))
