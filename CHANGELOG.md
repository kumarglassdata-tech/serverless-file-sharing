## 2026-07-02
- add test: special characters in filename are handled

## 2026-07-02
- docs: document mapping templates with inline JSON examples

## 2026-07-03
- update README deploy section with --parameter-overrides example

## 2026-07-03
- security: add Content-Security-Policy header to responses

## 2026-07-04
- add MAX_FILENAME_LENGTH constant (255 chars)

## 2026-07-04
- add pytest to requirements-dev.txt

## 2026-07-05
- add request validation for missing fileName param at API GW level

## 2026-07-06
- extract _validate_filename helper in UploadFunction

## 2026-07-06
- chore: normalise line endings to LF across lambda files

## 2026-07-06
- update samconfig.toml with us-east-1 as default region

## 2026-07-07
- docs: add project layout tree to README

## 2026-07-07
- docs: add step-by-step manual console deploy guide to README

## 2026-07-08
- chore: remove debug print left in DownloadFunction

## 2026-07-09
- security: validate Content-Type header on upload requests

## 2026-07-09
- add test: very long filename is rejected with 400

## 2026-07-09
- perf: set MemorySize to 256 MB for faster cold starts

