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

    revision_mode = "scm"
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }

    no_copy_source = True

    settings = "os", "compiler", "build_type", "arch"
    options = { "shared": [True, False] }
    default_options = { "shared": False }

    generators = "cmake_find_package"

    def build_requirements(self):
        self.test_requires("gtest/[^1.11.0]@")
        # self.tool_requires("cmake/[^3.23.1]@")

    def requirements(self):
        self.requires("fmt/[^8.1.1]@")

    def imports(self):
        self.copy("*.dll", src="@bindirs", dst=str(self.settings.build_type))
        self.copy("*.dylib*", src="@libdirs", dst="lib")

    def _get_configured_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_CONFIGURATION_TYPES"] = str(self.settings.build_type)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._get_configured_cmake()
        cmake.build()
        if not cross_building(self, skip_x64_x86=True):
            cmake.test()

    def package(self):
        cmake = self._get_configured_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libs = ['embo_lib']
        self.cpp_info.libdirs = ['lib']
        self.cpp_info.bindirs = ['bin']
