cmake_minimum_required(VERSION 3.22)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS ON)


# Define the build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Debug")
endif()

# Include toolchain file
include("cmake/gcc-arm-none-eabi.cmake")

# Enable compile command to ease indexing with e.g. clangd
set(CMAKE_EXPORT_COMPILE_COMMANDS TRUE)

enable_language(C ASM)

# Core project settings
project(h723)

# Create an executable object type
add_executable(${CMAKE_PROJECT_NAME})

# Add STM32CubeMX generated sources
add_subdirectory(cmake/stm32cubemx)

target_link_directories(${CMAKE_PROJECT_NAME} PRIVATE
    # Add user defined library search paths
)

target_sources(${CMAKE_PROJECT_NAME} PRIVATE
    # Add user sources here
)

target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE
    # Add user defined include paths
)

target_compile_definitions(${CMAKE_PROJECT_NAME} PRIVATE
    # Add user defined macros
)

target_link_libraries(${CMAKE_PROJECT_NAME}
    fun::run
)

set_target_properties(${CMAKE_PROJECT_NAME}
    PROPERTIES LINK_DEPENDS ${CMAKE_SOURCE_DIR}/stm32h723zgtx_flash.ld
)
