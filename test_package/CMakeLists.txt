cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(embo_app CXX)

set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN yes)

set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH $ORIGIN)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src/embo_app.cc
)

find_package(embo_lib REQUIRED)
target_link_libraries(${PROJECT_NAME}
    PRIVATE
        embo_lib::embo_lib
)
