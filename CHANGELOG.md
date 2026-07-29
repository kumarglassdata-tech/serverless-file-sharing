# Changelog

All notable changes to this project.

## 2026-07-22
- security: limit fileName to alphanumeric, dot, dash, underscore

## 2026-07-23
- refactor: extract S3 client initialisation into helper

## 2026-07-23
- add requirements-dev.txt separating test deps from runtime

## 2026-07-23
- fix: strip leading slash from fileName before S3 key lookup

## 2026-07-24
- add samconfig.toml with default deploy parameters

## 2026-07-24
- add architecture diagram to README

## 2026-07-25
- add test: empty body upload should succeed with empty file

## 2026-07-25
- security: reject fileName with null bytes

## 2026-07-25
- add events/upload_event.json for local Lambda testing

## 2026-07-26
- docs: add CHANGELOG entry for August improvements

## 2026-07-26
- refactor: move BUCKET_NAME to module-level constant

## 2026-07-26
- pin boto3 to >=1.28.0 in requirements.txt

## 2026-07-27
- chore: add Lambda description fields to template

## 2026-07-27
- docs: add CHANGELOG entry for September hardening

## 2026-07-27
- docs: add note about 10 MB API Gateway body limit

## 2026-07-28
- perf: reduce Lambda timeout to 15s (upload) and 10s (download)

## 2026-07-28
- add file extension allowlist to UploadFunction

## 2026-07-29
- fix: handle None body in UploadFunction without raising

## 2026-07-29
- block all public S3 access in CloudFormation config

