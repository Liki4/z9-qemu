# Publication boundary

The public repository must start with fresh Git history. Do not push a branch
of the private research repository, even if its latest tree excludes binaries.
Every reachable commit and staged blob belongs in the review.

Included: original emulator/tool source, formulas, interface addresses/masks,
sample-identification hashes, synthetic input generators, tests, documentation
and required open-source license notices.

Excluded: original or decrypted Nikon programs, firmware containers, camera
memory/flash dumps, keys, calibration images, extracted fonts/icons, copied
program instruction arrays, private photos, original UI screenshots and
runtime artifacts. Shader recognition uses hashes. The color knot coordinates
and indirect table selectors use formulas rather than embedded ROM tables.
Register masks and event mappings express interoperability behavior; they are
not a distribution of the original driver implementation.

`parameter_input.py` reads a default body from the user's local MAIN and creates
an explicit diagnostic ROM image only in the local run directory. No such
image is tracked or downloaded. Small synthetic version/selector/trailer
inputs are identified as assumptions, not recovered factory values.

The allowlist/manifest audit is an additional guard, not an automatic origin
or licensing determination. Maintainers must manually inspect new arrays,
fixtures, documentation and imports before refreshing it. A `.py` or `.c`
extension alone does not establish that a file is safe to publish.
