# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.fnal_art.fnal_github_package import *


class Dunedataprep(CMakePackage, FnalGithubPackage):
    """Dunedataprep"""

    repo = "DUNE/dunedataprep"
    version_patterns = ["09_00_00d00", "09.14.19"]

    version("10_00_03d00", sha256="673f451a37a0fb0884aa5f739af3bd66b15ef614e8e5c532d81c91c8c0ad65c5")
    version("09_92_00d00", sha256="6f636aa889a8b2e3b926c003e96bec098d79bc025417a2ae281750eb9ce0d57c")
    version("09_89_01d01", sha256="028bec795bf7da56b3acdd689110fa47498e9b3c766306b96ed14076c012642a")
    version("09_81_00d00", sha256="ac58dad4ac13bb742179b509bf3aab35a8fcbecd79364444342ca2ab69664dd7")
    version("develop", branch="develop", get_full_repo=True)

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch('v09_81_00d00.patch', when='@09_81_00d00')

    depends_on("dunecore")
    depends_on("jsonnet")
    depends_on("jsoncpp")
    depends_on("wirecell")
    depends_on("cetmodules", type="build")
    depends_on("cmake", type="build")
    depends_on("root+spectrum")
    
    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("IGNORE_ABSOLUTE_TRANSITIVE_DEPENDENCIES", "Bool:True"),
            self.define("WIRECELL_LIB", "%s" % self.spec["wirecell"].prefix.lib64)
        ] 
        return args

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
