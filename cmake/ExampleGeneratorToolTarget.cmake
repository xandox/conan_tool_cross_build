if(NOT TARGET example::generator)
    if(CMAKE_CROSSCOMPILING)
        find_program(EXAMPLE_GENERATOR_EXECUTABLE
            NAMES example-generator
            PATHS ENV PATH
            NO_DEFAULT_PATH
        )
    else()
        find_program(EXAMPLE_GENERATOR_EXECUTABLE
            NAMES example-generator 
            PATHS "${CMAKE_CURRENT_LIST_DIR}/../../bin/"
            NO_DEFAULT_PATH
        )
    endif()

    if(EXAMPLE_GENERATOR_EXECUTABLE)
        get_filename_component(EXAMPLE_GENERATOR_EXECUTABLE "${EXAMPLE_GENERATOR_EXECUTABLE}" ABSOLUTE)
        add_executable(example::generator IMPORTED)
        set_property(TARGET example::generator PROPERTY IMPORTED_LOCATION ${EXAMPLE_GENERATOR_EXECUTABLE})
    endif()
endif()
