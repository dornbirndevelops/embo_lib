from conans import ConanFile, CMake
from conans.tools import cross_building

class EmboLibRecipe(ConanFile):
    name = "embo_lib"
    version = "1.0.0"

    license = "feel free to use it"
    author = "Alexander Dengg dornbirndevelops@gmail.com"
    url = "https://github.com/dornbirndevelops/embo_lib"
    description = "demo project for Embo++ conference containing an example library implementation using Conan"
    topics = ("conan", "embo", "example")

    settings = "os", "compiler", "build_type", "arch"
    options = { "shared": [True, False] }
    default_options = { "shared": False }

    generators = "cmake_find_package"

    revision_mode = "scm"
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }

    def build_requirements(self):
        self.test_requires("gtest/[^1.11.0]@")
        # self.tool_requires("protobuf/[^3.19.2]@")

    def requirements(self):
        self.requires("fmt/[^8.1.1]@")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if not cross_building(self, skip_x64_x86=True):
            cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["embo_lib"]
