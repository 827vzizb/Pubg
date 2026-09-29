[app]

title = PUBG Game Launcher
package.name = pubggamelauncher
package.domain = org.launcher

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0.0

# FIX 1: "android" hata diya - ye recipe nahi hai, aur cython pin kiya
requirements = python3,kivy==2.3.0

orientation = landscape
fullscreen = 1

# ---- Android build settings (ye pehle missing the) ----
android.accept_sdk_license = True
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# FIX 4: sirf arm64 (A36 aur sab modern phone isi par chalte hain)
android.archs = arm64-v8a

android.permissions = INTERNET
android.allow_backup = True

# p4a stable branch use karo (buildozer 1.5.0 ke saath match karta hai)
p4a.branch = master

# Optional - apna icon/presplash agar rakha ho
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
