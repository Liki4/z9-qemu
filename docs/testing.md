# Validation status

The standalone launcher passed three native MENU returns on 2026-10-10,
with fresh RAW/LCD video and four independent pixel checks. Three preceding
cold boots of the same functional profile also passed, including a run with
detailed tracing removed. These are bounded functional tests, not physical
camera qualification or indefinite stability coverage.

| Run | Configuration | Initial RAW/video | Return 1 | Return 2 | Return 3 |
| --- | --- | --- | --- | --- | --- |
|405|Candidate, sparse submission trace|1403/69|1517/293|1628/511|1734/724|
|406|Candidate, no detailed trace|1406/72|1521/296|1634/518|1746/738|
|407|Candidate, CPU3 wait-site counts|1401/66|1512/284|1624/505|1735/722|
|408|Standalone source launcher, no private wrapper/plugin|1403/68|1512/286|1621/503|1732/721|

Every menu in these runs was reached with one press. Run408 compares610,199
clear-alpha pixels at each live-view stage. Mean absolute RGB error is
0.1508–0.1521/255, maximum0.624; luminance standard deviation exceeds60.
The owned emulator stopped normally, without a recorded error. The test
input was synthetic640×480 RGGB12/u16 color bars, not a Nikon sensor dump.

Run408 result SHA-256:
`498601b76356c82c2fa8ee49a04a1e0fe508176f57a1a491c38eaad23d53dbcf`.
Tested executable SHA-256:
`72e2b48214af7477e7bdee4afd86a320afc71f4b71ac570c7ffa4fc062aa26b9`.
The original firmware fingerprint is in [firmware input](firmware.md).
Full runtime evidence stays private because it includes firmware-derived
memory planes and UI captures. These hashes identify local evidence; the
source repository does not distribute those artifacts.

The public build also passes13 firmware-free WFE/SEV/IRQ execution checks,
9 Python tests, pixel tests, default-off board realization and rejection of
unsupported CPU/clock settings. These test the
[documented service event contract](service-events.md), not complete ARM
event architecture. Patch application and repeated preparation were checked.

The private Z9 C5.32 baseline has independently demonstrated 915 RAW-derived
frames, 5,174,830,080 pixel bytes, zero rejected destinations and 1,144 video
scanouts. For 610,199 clear-alpha LCD pixels, an independent NV12 decode had
mean RGB absolute error 0.243/255 and maximum error 0.524. This establishes the
functional pixel path for that recorded run, not physical sensor accuracy.

Source drain tests execute original driver and ISR routines with explicitly
prepared diagnostic state. Masked pending, unmask, unrelated W1C, reset and
restart are checked. The RAW DMA regression checks destination guards,
backpressure and complete-bank replacement. These tests are local because
they require the user's proprietary firmware and are not public CI inputs.

Public CI will run only synthetic source/RAW/protocol tests, publication audit
and a verified upstream build. It cannot boot the camera UI without firmware.
Do not interpret a green CI badge as camera acceptance.

Remaining physical limits include real CMOS programming, sensor timing,
calibration, AE/AF/PDAF, recording, storage writing and complete GPU behavior.

The current display correction isolates directly enabled NV12 video from the
two optional layer controls. Ten fixed-pixel checks cover layer combinations,
direct stop/restart, source preservation and strict MMIO. Fourteen existing
display/alpha/IRQ/bounds checks also pass on the corrected standalone build.
QOM `last_frame_has_video` describes the last composed frame; the video frame
counter remains historical. MENU acceptance requires both new RAW and new LCD
video after returning, followed by independent pixel validation.

Earlier native menu-return diagnostics exposed premature frame release during
submission. MVD interrupt delivery and acknowledgement lifetime were
corrected in separate original-ISR checks, but this does not establish restart
acceptance. A further unsupported two-byte plane clear was captured and its
functional support now passes 184 local clear checks, including full-buffer
comparison and invalid-request boundaries. Diagnostic MVD scheduling changes
are excluded from this launcher. The current combined service-event,
instruction-clock, virtual-input and synthetic-timing profile passes the
three-return acceptance above. The historical failing observations remain
valid evidence for the earlier profiles; no single component is claimed as
an independently proved cure for every lifetime failure.
