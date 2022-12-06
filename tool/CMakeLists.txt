
project(example-generator CXX)

find_package(ZLIB CONFIG REQUIRED)

add_executable(example-generator example-generator.cpp)
target_link_libraries(example-generator PRIVATE ZLIB::ZLIB)

install(TARGETS example-generator DESTINATION bin)
