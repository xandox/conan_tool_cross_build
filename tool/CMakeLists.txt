
project(example-generator CXX)

find_package(ZLIB CONFIG REQUIRED)
find_package(spdlog CONFIG REQUIRED)
find_package(flatbuffers CONFIG REQUIRED)

add_executable(example-generator example-generator.cpp)
target_link_libraries(example-generator PRIVATE ZLIB::ZLIB spdlog::spdlog flatbuffers::flatbuffers)

if (NOT TARGET flatbuffers::flatc)
    message(FATAL_ERROR "flatbuffers::flatc target not found.")
endif()

install(TARGETS example-generator DESTINATION bin)
