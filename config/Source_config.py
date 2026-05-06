# config/Source_config.py
Arch_SOURCES = {
    "core": [
        "https://wiki.archlinux.org/title/Installation_guide",
        "https://wiki.archlinux.org/title/General_recommendations",
        "https://wiki.archlinux.org/title/Users_and_groups",
        "https://wiki.archlinux.org/title/Pacman",
        "https://wiki.archlinux.org/title/Arch_User_Repository",
        "https://wiki.archlinux.org/title/Systemd",
        "https://wiki.archlinux.org/title/System_maintenance",
        "https://wiki.archlinux.org/title/General_troubleshooting",
        "https://wiki.archlinux.org/title/AUR_helpers",
        "https://wiki.archlinux.org/title/Pacman/Tips_and_tricks",
        "https://wiki.archlinux.org/title/Kernel_parameters" 
    ],
    "hardware": [
        "https://wiki.archlinux.org/title/NVIDIA",
        "https://wiki.archlinux.org/title/AMDGPU",
        "https://wiki.archlinux.org/title/Intel_graphics",
        "https://wiki.archlinux.org/title/Bluetooth",
        "https://wiki.archlinux.org/title/Microcode",
        "https://wiki.archlinux.org/title/Laptop",          
        "https://wiki.archlinux.org/title/Power_management"
    ],
    "desktop": [
        "https://wiki.archlinux.org/title/Wayland",
        "https://wiki.archlinux.org/title/NetworkManager",
        "https://wiki.archlinux.org/title/PipeWire",
        "https://wiki.archlinux.org/title/Environment_variables",
        "https://wiki.archlinux.org/title/XDG_Desktop_Portal",
        "https://wiki.archlinux.org/title/Fonts",
        "https://wiki.archlinux.org/title/Hyprland",
        "https://wiki.archlinux.org/title/SDDM",
        "https://wiki.archlinux.org/title/Desktop_notifications",
        "https://wiki.archlinux.org/title/Cursor_themes"
    ],
    "filesystem": [
        "https://wiki.archlinux.org/title/Btrfs",
        "https://wiki.archlinux.org/title/Partitioning",
        "https://wiki.archlinux.org/title/Fstab",
        "https://wiki.archlinux.org/title/Swap",
        "https://wiki.archlinux.org/title/Ext4"
    ],
    "bootloader": [
        "https://wiki.archlinux.org/title/GRUB",
        "https://wiki.archlinux.org/title/Systemd-boot",
        "https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface"
    ],
    "security": [
        "https://wiki.archlinux.org/title/Sudo",
        "https://wiki.archlinux.org/title/Polkit",
        "https://wiki.archlinux.org/title/Security",
        "https://wiki.archlinux.org/title/Dm-crypt/Encrypting_an_entire_system",
        "https://wiki.archlinux.org/title/UFW"
    ],
    "power_user_gaming": [
        "https://wiki.archlinux.org/title/Gaming",
        "https://wiki.archlinux.org/title/Steam",
        "https://wiki.archlinux.org/title/Wine",
        "https://wiki.archlinux.org/title/Proton",
        "https://wiki.archlinux.org/title/Improving_performance"
    ]
}

ADDITIONAL_SOURCES = {
    "hyprland_deep_dive": [
        "https://wiki.hypr.land/Configuring/Basics/Variables",
        "https://wiki.hypr.land/Configuring/Basics/Monitors",
        "https://wiki.hypr.land/Configuring/Basics/Binds",
        "https://wiki.hypr.land/Configuring/Basics/Dispatchers",
        "https://wiki.hypr.land/Configuring/Basics/Window-Rules",
        "https://wiki.hypr.land/Configuring/Basics/Workspace-Rules",
        "https://wiki.hypr.land/Configuring/Start",
        "https://wiki.hypr.land/Configuring/Layouts/Dwindle-Layout",
        "https://wiki.hypr.land/Configuring/Master-Layout",
        "https://wiki.hypr.land/Configuring/Scrolling-Layout",
        "https://wiki.hypr.land/Configuring/Monocle-Layout",
        "https://wiki.hypr.land/Configuring/Advanced-and-Cool/Animations",
        "https://wiki.hypr.land/Configuring/Advanced-and-Cool/Devices",
        "https://wiki.hypr.land/Configuring/Advanced-and-Cool/Tearing",
        "https://wiki.hypr.land/Configuring/Advanced-and-Cool/Permissions",
        "https://wiki.hypr.land/Configuring/Advanced-and-Cool/XWayland",
        "https://wiki.hypr.land/Configuring/Advanced-and-Cool/Environment-variables",
        "https://wiki.hypr.land/Configuring/Advanced-and-Cool/Multi-GPU",
        "https://wiki.hypr.land/Configuring/Advanced-and-Cool/Performance",
        "https://wiki.hypr.land/Configuring/Advanced-and-Cool/Using-hyprctl",
        "https://wiki.hypr.land/Crashes-and-Bugs",
        "https://wiki.hypr.land/FAQ",
        "https://wiki.hypr.land/Nvidia",
        "https://wiki.hypr.land/IPC",
        "https://wiki.hypr.land/Plugins/Using-Plugins",
        "https://wiki.hypr.land/Plugins/Development/Getting-Started",
        "https://wiki.hypr.land/Plugins/Development/Plugin-Guidelines",
        "https://wiki.hypr.land/Plugins/Development/Advanced",
        "https://wiki.hypr.land/Hypr-Ecosystem/hypridle",
        "https://wiki.hypr.land/Hypr-Ecosystem/hyprlock",
        "https://wiki.hypr.land/Hypr-Ecosystem/hyprpaper",
        "https://wiki.hypr.land/Hypr-Ecosystem/xdg-desktop-portal-hyprland",
        "https://wiki.hypr.land/Hypr-Ecosystem/hyprpolkitagent",
    ],
    "zsh_ecosystem": [
        "https://wiki.archlinux.org/index.php?title=Zsh&action=raw",
        "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/README.md",
        "https://raw.githubusercontent.com/zsh-users/zsh-autosuggestions/master/README.md",
        "https://raw.githubusercontent.com/zsh-users/zsh-syntax-highlighting/master/README.md",
        "https://raw.githubusercontent.com/romkatv/powerlevel10k/master/README.md",
        "https://raw.githubusercontent.com/mattmc3/antidote/main/README.md"
    ],
    "jakoolit_specifics": [
        "https://raw.githubusercontent.com/JaKooLit/Hyprland-Dots/main/README.md",
        "https://raw.githubusercontent.com/JaKooLit/Hyprland-Dots/main/config/hypr/scripts/Refresh.sh",
        "https://raw.githubusercontent.com/JaKooLit/Hyprland-Dots/main/config/hypr/scripts/Volume.sh",
        "https://raw.githubusercontent.com/JaKooLit/Hyprland-Dots/main/config/hypr/configs/Keybinds.conf",
        "https://raw.githubusercontent.com/JaKooLit/Hyprland-Dots/main/config/hypr/configs/ENVariables.conf",
        "https://raw.githubusercontent.com/JaKooLit/Hyprland-Dots/main/config/hypr/configs/Settings.conf"
    ],
    "wayland_essentials": [
        "https://wiki.archlinux.org/index.php?title=Wayland&action=raw",
        "https://wiki.archlinux.org/index.php?title=XDG_Desktop_Portal&action=raw",
        "https://raw.githubusercontent.com/swaywm/swaybg/master/README.md",
        "https://raw.githubusercontent.com/Alexays/Waybar/master/README.md",
        "https://raw.githubusercontent.com/davatorium/rofi/next/README.md"
    ]
}