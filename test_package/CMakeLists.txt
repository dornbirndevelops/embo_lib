cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(embo_app CXX)

set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN yes)
if(NOT APPLE)
    set(CMAKE_INSTALL_RPATH $ORIGIN)
    set(CMAKE_BUILD_WITH_INSTALL_RPATH on)
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src/embo_app.cc
)

target_link_libraries(${PROJECT_NAME}
    PRIVATE
        ${CONAN_LIBS}
)
