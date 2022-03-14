from conans import ConanFile, CMake
from conans.tools import cross_building
from os.path import join

class EmboLibTestRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not cross_building(self):
            self.run(join("bin", "embo_app"), run_environment=True)
