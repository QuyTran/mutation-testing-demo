rm tutorial_devide.sqlite
cosmic-ray init tutorial_devide.toml tutorial_devide.sqlite
cosmic-ray --verbose baseline tutorial_devide.toml
cr-report tutorial_devide.sqlite --show-pending
cosmic-ray exec tutorial_devide.toml tutorial_devide.sqlite
cr-html tutorial_devide.sqlite > report_devide.html
open report_devide.html
