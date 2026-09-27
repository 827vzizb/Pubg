[app]
title = PUBG Game Launcher
package.name = pubggamelauncher
package.domain = org.launcher
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy,android

# PUBG style horizontal view aur SDK license fix
orientation = landscape
fullscreen = 1
android.accept_sdk_license = True
android.ndk = 25b

android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
