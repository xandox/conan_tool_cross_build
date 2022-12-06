
project(example-lib CXX)

add_library(${PROJECT_NAME} STATIC example-lib.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

install(FILES example-lib.hpp DESTINATION include)
install(TARGETS ${PROJECT_NAME} DESTINATION lib)
