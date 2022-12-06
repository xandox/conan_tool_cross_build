cmake_minimum_required(VERSION 3.24)

project(test_package)

find_package(example CONFIG REQUIRED)
add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} example::example)

add_custom_command(OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/generated.cpp ${CMAKE_CURRENT_BINARY_DIR}/generated.h
									 COMMAND example::generator ${CMAKE_CURRENT_BINARY_DIR})

target_sources(${PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/generated.cpp)
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_BINARY_DIR})
