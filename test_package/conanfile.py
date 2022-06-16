from conans import ConanFile, CMake
from conans.tools import cross_building
from os.path import join

class EmboLibTestRecipe(ConanFile):
    test_type = "explicit"

    settings = "os", "compiler", "build_type", "arch"

    generators = "cmake_find_package"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def imports(self):
        self.copy("*.dll", src="@bindirs", dst=str(self.settings.build_type))
        self.copy("*.dylib*", src="@libdirs", dst="lib")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if cross_building(self):
            return

        app_path = join(str(self.settings.build_type) if self.settings.get_safe("compiler") in ("Visual Studio", "msvc") else ".", "app")
        self.run(app_path)
