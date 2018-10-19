#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_default
import os

if __name__ == "__main__":

    builder = build_template_default.get_builder()
	
    if os.environ.get('EMSCRIPTEN_VERSIONS'):
        for version in os.environ['EMSCRIPTEN_VERSIONS'].split(','):
            for build_type in os.environ.get('CONAN_BUILD_TYPES','Debug').split(','):
                builder.add(settings={
                    "compiler": "emcc",
                    "compiler.libcxx":'libcxxabi',
                    "build_type": build_type, 
                    "compiler.version": version
                    })

        items = []
        for item in builder.items:
            if not os.environ.get('CONAN_GCC_VERSIONS') and item.settings['compiler'] == 'gcc':
                continue  
            if not os.environ.get('CONAN_CLANG_VERSIONS') and item.settings['compiler'] == 'clang':
                continue 
            items.append(item)

        builder.items = items
    builder.run()
