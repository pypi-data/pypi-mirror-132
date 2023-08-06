cmake_minimum_required(VERSION 3.15)

set(CMAKE_POSITION_INDEPENDENT_CODE ON) # for -fPIC

project(nkf LANGUAGES CXX C)

add_executable(nkf
    ${CMAKE_CURRENT_SOURCE_DIR}/nkf.c
    ${CMAKE_CURRENT_SOURCE_DIR}/utf8tbl.c
)

add_library(libnkf SHARED
    ${CMAKE_CURRENT_SOURCE_DIR}/libnkf.h
    ${CMAKE_CURRENT_SOURCE_DIR}/libnkf.cpp
)

add_library(libnkf_static STATIC
    ${CMAKE_CURRENT_SOURCE_DIR}/libnkf.h
    ${CMAKE_CURRENT_SOURCE_DIR}/libnkf.cpp
)

install(
    TARGETS nkf libnkf_static
    RUNTIME    DESTINATION bin
    LIBRARY    DESTINATION lib
)

install(
    TARGETS libnkf
    RUNTIME    DESTINATION lib ## for windows dll
    LIBRARY    DESTINATION lib
)

install(
    FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/libnkf.h
    DESTINATION include
)
