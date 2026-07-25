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

