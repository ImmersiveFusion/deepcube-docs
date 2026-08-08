# Installing on macOS

!!! warning "Experimental"
    The macOS build of DeepCube is still considered experimental and not fully supported. Additional manual steps are required.

## Steam

!!! info "Windows Only"
    Steam is currently available for Windows only. macOS support on Steam is planned for a future release.

Learn more about [Steam](https://store.steampowered.com/about/){ target="_blank" } on their website.

## Offline Installer (DMG)

!!! info "Alpha channel only on macOS"
    The macOS build of DeepCube is currently published to the **alpha** channel only. Stable and beta DMGs are not yet available. Windows builds on all three channels remain available from the [Windows installation page](../Windows/index.md).

[Latest Alpha Build :material-download:](https://downloads.immersivefusion.com/release/alpha/DC.latest.dmg){ .md-button }

1. Click on the button above to download the installer for DeepCube for macOS from the cloud. The file size is around `1.5GB`

1. Open the Disk Image file (DMG) and drag `DC.app` to your `Applications` folder.

1. Open `Terminal` and execute the following command to remove `DC` from quarantine.

```bash
xattr -d com.apple.quarantine /Applications/DC.app
```
