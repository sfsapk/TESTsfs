[app]
title = Rocket_Editor
package.name = rocket_editor
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
source.include_patterns = data/**
source.exclude_dirs = tests, bin, data/.git, __pycache__, .buildozer
# Используем version.regex вместо version
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/version.py
requirements = python3,kivy==2.1.0,pillow,json5,plyer
orientation = portrait
fullscreen = 0

# Android specific
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 31
android.ndk = 23b
android.minapi = 21
android.arch = arm64-v8a, armeabi-v7a
android.buildtools_version = 31.0.0
android.androidx = True
android.presplash_color = #FFFFFF

# Buildozer
[buildozer]
log_level = 2
warn_on_root = 1
build_dir = ./.buildozer
bin_dir = ./bin
skip_update = True
