import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan import tools

class ToolAndLibPackage(ConanFile):
    name = "example"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    exports_sources = "CMakeLists.txt", "lib/*", "tool/*", "cmake/*"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def requirements(self):
        self.requires("zlib/1.2.13")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    @property
    def _module_path(self):
        return os.path.join("lib", "cmake")

    def package(self):
        cmake = CMake(self)
        cmake.install()
        tools.files.copy(
            self,
            "ExampleGeneratorToolTarget.cmake",
            src=os.path.join(self.source_folder, "cmake"),
            dst=os.path.join(self.package_folder, self._module_path),
        )

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "example")
        self.cpp_info.set_property("cmake_target_name", "example::example")
        self.cpp_info.libs = self.collect_libs()
        build_modules = [
            os.path.join(self._module_path, "ExampleGeneratorToolTarget.cmake"),
        ]
        self.cpp_info.set_property("cmake_build_modules", build_modules)
        bindir = os.path.join(self.package_folder, "bin")
        self.output.info("Appending PATH environment variable: {}".format(bindir))
        self.env_info.PATH.append(bindir)
