from conan import ConanFile
from conan.tools.build import cross_building
from conan.tools.cmake import CMake, cmake_layout, CMakeToolchain, CMakeDeps
from conan.tools.files import copy
from os.path import join

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

    generators = "CMakeToolchain", "CMakeDeps"

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

    def layout(self):
        cmake_layout(self)

        self.cpp.source.includedirs = ["include"]
        self.cpp.build.includedirs = ["."] # generated export headers
        self.cpp.build.libs = ["embo_lib"]
        self.cpp.package.includedirs = ["include"]
        self.cpp.package.libs = ["embo_lib"]
        self.cpp.package.libdirs = ["lib"]
        self.cpp.package.bindirs = ["bin"]

    def generate(self):
        CMakeToolchain(self).generate()
        CMakeDeps(self).generate()
        bindir = join(self.build_folder, self.cpp.build.bindirs[0])
        for dep in self.dependencies.values():
            copy(self, "*.dll", dep.cpp_info.bindirs[0], bindir)
            copy(self, "*.dylib*", dep.cpp_info.libdirs[0], bindir)
            copy(self, "*.so*", dep.cpp_info.libdirs[0], bindir)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if not cross_building(self, skip_x64_x86=True):
            cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()
