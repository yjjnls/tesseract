cmake_minimum_required(VERSION 3.1)
project(cmake_wrapper)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(CMAKE_SYSTEM_NAME STREQUAL Emscripten)
    set(CMAKE_FIND_ROOT_PATH ${CMAKE_FIND_ROOT_PATH} ${CONAN_CMAKE_MODULE_PATH})
endif()

include("CMakeListsOriginal.txt")
