cmake_minimum_required(VERSION 3.15)
project(embo_lib CXX)

set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN yes)
if(NOT APPLE)
    set(CMAKE_INSTALL_RPATH $ORIGIN)
endif()

add_library(${PROJECT_NAME})

set_target_properties(
    ${PROJECT_NAME} PROPERTIES
        SOVERSION   1
        VERSION     1.0.0
)

include(GenerateExportHeader)
generate_export_header(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
    PUBLIC
        ${CMAKE_CURRENT_BINARY_DIR}/embo_lib_export.h
        ${CMAKE_CURRENT_SOURCE_DIR}/include/embo_lib.hh
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src/embo_lib.cc
)

target_include_directories(${PROJECT_NAME}
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

find_package(fmt REQUIRED)
target_link_libraries(${PROJECT_NAME}
    PRIVATE
        fmt::fmt
)

get_target_property(_PUBLIC_HEADERS ${PROJECT_NAME} INTERFACE_SOURCES)
set_target_properties(
    ${PROJECT_NAME} PROPERTIES
        PUBLIC_HEADER "${_PUBLIC_HEADERS}"
)
unset(_PUBLIC_HEADERS)

install(TARGETS ${PROJECT_NAME})

if(NOT CMAKE_CROSSCOMPILING)
    add_executable(${PROJECT_NAME}_test)
    
    target_sources(${PROJECT_NAME}_test
        PRIVATE
            ${CMAKE_CURRENT_SOURCE_DIR}/test/embo_lib_test.cc
    )

    find_package(GTest REQUIRED)
    target_link_libraries(${PROJECT_NAME}_test
        PRIVATE
            ${PROJECT_NAME}
            GTest::gtest
            GTest::gtest_main
    )

    enable_testing()
    include(GoogleTest)
    gtest_discover_tests(${PROJECT_NAME}_test
        DISCOVERY_MODE PRE_TEST
    )
endif()
