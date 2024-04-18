from spack.package import *

class DuneTms(CMakePackage):
    """dune-tms -- TMS reconstruction and simulation """

    license("MIT")
    homepage = "https://github.com/DUNE/dune-tms"
    git = "https://github.com/DUNE/dune-tms.git"

    executables = ["^BField_tester$",
                   "^BetheBloch_Example$",
                   "^CherryPickEvents$",
                   "^ConvertToTMSTree$",
                   "^DBSCAN_test$",
                   "^DrawEvents$",
                   "^ShootRay$",
                   "^TrackLengthTester$"]

    maintainers("LiamOS") # Maintainer on FNAL spack 'n github

    version("main", branch="main")
    version("develop", branch="main")

    depends_on("cmake", type="build")
    depends_on("nlohmann-json")
    depends_on("edep-sim")
    #depends_on("root")
    #depends_on("geant4")

    def setup_run_environment(self, env): 
        env.set("TMS_DIR", self.prefix)

class CMakeBuilder(spack.build_systems.cmake.CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define("CMAKE_VERBOSE_MAKEFILE", True)
        ]  
        return args
