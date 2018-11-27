#!/usr/bin/env python
from conanos.build import Main
from conan.packager import ConanMultiPackager
import os
import platform

if __name__ == "__main__":    
    builder = ConanMultiPackager(docker_entry_script='/bin/bash -c ~/emsdk/emsdk_env.sh')

    if os.environ.get('EMSCRIPTEN_VERSIONS'):
        for version in os.environ['EMSCRIPTEN_VERSIONS'].split(','):
            for build_type in os.environ.get('CONAN_BUILD_TYPES','Debug').split(','):
                builder.add(settings={
                    "arch": os.environ.get('CONAN_ARCHS','x86_64'), 
                    "compiler": "emcc",
                    "compiler.libcxx":'libstdc++11',
                    "build_type": build_type, 
                    "compiler.version": version
                    },
                    options={}, env_vars={}, build_requires={})

        items = []
        for item in builder.items:
            if not os.environ.get('CONAN_GCC_VERSIONS') and item.settings['compiler'] == 'gcc':
                continue  
            if not os.environ.get('CONAN_CLANG_VERSIONS') and item.settings['compiler'] == 'clang':
                continue 
            items.append(item)

        builder.items = items


    builder.run()