#include <iostream>
#include <fstream>
#include <filesystem>

int main(int argc, char** argv) {
	if (argc != 2) {
		std::cerr << "Usage: " << argv[0] << " <output-directory>" << std::endl;
		return 1;
	}

	auto output_dir = std::filesystem::path{argv[1]};
	create_directories(output_dir);

	auto header_file = output_dir / "generated.hpp";
	auto source_file = output_dir / "generated.cpp";

	{
		std::ofstream header{header_file, std::ios::out | std::ios::binary};
		header << "#pragma once\n";
		header << "namespace generated_example {\n";
		header << "void hello();\n";
		header << "}\n";
	}

	{
		std::ofstream source{source_file, std::ios::out | std::ios::binary};
		source << "#include \"generated.hpp\"\n";
		source << "#include <iostream>\n";
		source << "namespace generated_example {\n";
		source << "void hello() {\n";
		source << "std::cout << \"Hello from generated!\" << std::endl;\n";
		source << "}\n";
		source << "}\n";
	}

	return 0;
}
