# This package.py written by Liam O'Sullivan <liam.osullivan@uni-mainz.de>
# For reasons™, explicitly including root and geant4 as dependencies
# causes the build to fail (missing blas or whatevs).
# If you spack load root and geant4 it builds fine though.

from spack.package import *

class NdCafmaker(MakefilePackage):
    """ND-CAFMaker-- Makes CAFs for the ND"""

    license("Apache-2.0")
    homepage = "https://github.com/DUNE/ND_CAFMaker"
    git = "https://github.com/DUNE/ND_CAFMaker.git"

    executables = ["^MakeCAF$"]

    maintainers("LiamOS") # Feel free to join me

    version("main", branch="main")
    version("develop", branch="main")
    version("tms", branch="tms_caf_update")
    version("4.6.3", tag="v4.6.3")

    #depends_on("gcc", type="build")
    depends_on("duneanaobj")
    depends_on("log4cpp")
    depends_on("ifdhc")
    depends_on("h5cpp")
    depends_on("hdf5+cxx")
    depends_on("eigen")
    depends_on("py-pycurl")
    depends_on("geant4")
    depends_on("dk2nugenie")
    depends_on("genie-xsec")
    depends_on("genie-phyopt")
    depends_on("fhicl-cpp")
    depends_on("libxml2")
    depends_on("pythia6")
    depends_on("tbb")
    depends_on("gsl")

    def edit(self, spec, prefix):
        return

    def setup_build_environment(self, env): 
        #env.set("TMS_DIR", self.prefix)
        env.set("BOOST_INC", "%s" % self.spec["boost"].prefix.include)
        env.set("LOG4CPP_INC", "%s" % self.spec["log4cpp"].prefix.include)
        env.set("CETLIB_INC", "%s" % self.spec["cetlib"].prefix.include)
        env.set("CETLIB_EXCEPT_INC", "%s" % self.spec["cetlib"].prefix.include)
        env.set("FHICLCPP_INC", "%s" % self.spec["fhicl-cpp"].prefix.include)
        env.set("DUNEANAOBJ_INC", "%s" % self.spec["duneanaobj"].prefix.include)
        env.set("GENIE_INC", "%s" % self.spec["genie"].prefix.include)
        env.set("HDF5_INC", "%s" % self.spec["hdf5"].prefix.include)
        env.set("H5CPP_INC", "%s/h5cpp/" % self.spec["h5cpp"].prefix.include)
        env.set("ROOT_INC", "%s" % self.spec["root"].prefix.include)
        env.set("FHICLCPP_LIB", "%s" % self.spec["fhicl-cpp"].prefix.lib)
        env.set("LOG4CPP_LIB", "%s" % self.spec["log4cpp"].prefix.lib)
        env.set("GSL_LIB", "%s" % self.spec["gsl"].prefix.lib)
        env.set("TBB_LIB", "%s" % self.spec["tbb"].prefix.lib)
        env.set("DUNEANAOBJ_LIB", "%s" % self.spec["duneanaobj"].prefix.lib)
        env.set("HDF5_LIB", "%s" % self.spec["hdf5"].prefix.lib)


#    def setup_run_environment(self, env): 
#        env.set("TMS_DIR", self.prefix)

#class MakefileBuilder(spack.build_systems.cmake.CMakeBuilder):
#    
#    def cmake_args(self):
#        args = [
#            self.define("CMAKE_VERBOSE_MAKEFILE", True)
#        ]  
#        return args
