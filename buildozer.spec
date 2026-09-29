[app]

title = PUBG Game Launcher
package.name = pubggamelauncher
package.domain = org.launcher

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0.0

# Sirf ye do - "android" recipe nahi hai, isliye kabhi mat likhna
requirements = python3,kivy==2.3.0

orientation = landscape
fullscreen = 1

android.accept_sdk_license = True
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Sirf ek architecture - A36 arm64 hai, armeabi-v7a ki zaroorat nahi
android.archs = arm64-v8a

android.permissions = INTERNET
android.allow_backup = True
android.log_level = 2

p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
