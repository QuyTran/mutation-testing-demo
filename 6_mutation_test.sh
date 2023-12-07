rm tutorial_prime.sqlite
cosmic-ray init tutorial_prime.toml tutorial_prime.sqlite
cosmic-ray --verbose baseline tutorial_prime.toml
cr-report tutorial_prime.sqlite --show-pending
cosmic-ray exec tutorial_prime.toml tutorial_prime.sqlite
cr-html tutorial_prime.sqlite > report_prime.html
open report_prime.html
