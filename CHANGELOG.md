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

## 2026-07-29
- improve README with troubleshooting section

## 2026-07-30
- improve error messages to include context

## 2026-07-30
- add structured logging to UploadFunction for CloudWatch visibility

## 2026-07-30
- refactor: consolidate _response helper across both functions

## 2026-07-31
- chore: bump Python runtime to 3.12 in template.yaml

## 2026-07-31
- docs: add security section to README

## 2026-08-01
- docs: update CHANGELOG for October patch release

## 2026-08-01
- fix: DownloadFunction should not expose raw S3 error to client

## 2026-08-02
- perf: reuse boto3 S3 client across Lambda invocations

## 2026-08-02
- add test: DownloadFunction returns correct Content-Type

## 2026-08-03
- add 100 MB file size guard in UploadFunction

## 2026-08-03
- docs: clarify fileName query param is required in README

## 2026-08-03
- docs: add badge for Python version to README

## 2026-08-04
- improve API Gateway 4xx and 5xx response shapes

## 2026-08-05
- add curl examples for each error scenario to README

## 2026-08-05
- chore: housekeeping 2026-08-05

## 2026-08-06
- chore: housekeeping 2026-08-06

## 2026-08-06
- chore: housekeeping 2026-08-06

## 2026-08-06
- chore: housekeeping 2026-08-06

## 2026-08-07
- chore: housekeeping 2026-08-07

## 2026-08-07
- chore: housekeeping 2026-08-07

## 2026-08-08
- chore: housekeeping 2026-08-08

## 2026-08-08
- chore: housekeeping 2026-08-08

## 2026-08-09
- chore: housekeeping 2026-08-09

## 2026-08-09
- chore: housekeeping 2026-08-09

## 2026-08-09
- chore: housekeeping 2026-08-09

## 2026-08-10
- chore: housekeeping 2026-08-10

## 2026-08-10
- chore: housekeeping 2026-08-10

## 2026-08-11
- chore: housekeeping 2026-08-11

## 2026-08-11
- chore: housekeeping 2026-08-11

## 2026-08-12
- chore: housekeeping 2026-08-12

## 2026-08-13
- chore: housekeeping 2026-08-13

## 2026-08-13
- chore: housekeeping 2026-08-13

## 2026-08-14
- chore: housekeeping 2026-08-14

## 2026-08-14
- chore: housekeeping 2026-08-14

## 2026-08-15
- chore: housekeeping 2026-08-15

## 2026-08-15
- chore: housekeeping 2026-08-15

## 2026-08-16
- chore: housekeeping 2026-08-16

## 2026-08-16
- chore: housekeeping 2026-08-16

## 2026-08-16
- chore: housekeeping 2026-08-16

## 2026-08-17
- chore: housekeeping 2026-08-17

## 2026-08-17
- chore: housekeeping 2026-08-17

## 2026-08-17
- chore: housekeeping 2026-08-17

## 2026-08-18
- chore: housekeeping 2026-08-18

## 2026-08-18
- chore: housekeeping 2026-08-18

## 2026-08-18
- chore: housekeeping 2026-08-18

## 2026-08-19
- chore: housekeeping 2026-08-19

## 2026-08-19
- chore: housekeeping 2026-08-19

## 2026-08-20
- chore: housekeeping 2026-08-20

## 2026-08-21
- chore: housekeeping 2026-08-21

## 2026-08-21
- chore: housekeeping 2026-08-21

## 2026-08-22
- chore: housekeeping 2026-08-22

## 2026-08-22
- chore: housekeeping 2026-08-22

## 2026-08-22
- chore: housekeeping 2026-08-22

## 2026-08-23
- chore: housekeeping 2026-08-23

## 2026-08-23
- chore: housekeeping 2026-08-23

## 2026-08-24
- chore: housekeeping 2026-08-24

## 2026-08-24
- chore: housekeeping 2026-08-24

## 2026-08-24
- chore: housekeeping 2026-08-24

## 2026-08-25
- chore: housekeeping 2026-08-25

## 2026-08-25
- chore: housekeeping 2026-08-25

## 2026-08-25
- chore: housekeeping 2026-08-25

## 2026-08-26
- chore: housekeeping 2026-08-26

## 2026-08-26
- chore: housekeeping 2026-08-26

## 2026-08-26
- chore: housekeeping 2026-08-26

## 2026-08-27
- chore: housekeeping 2026-08-27

## 2026-08-27
- chore: housekeeping 2026-08-27

## 2026-08-27
- chore: housekeeping 2026-08-27

## 2026-08-28
- chore: housekeeping 2026-08-28

## 2026-08-28
- chore: housekeeping 2026-08-28

## 2026-08-29
- chore: housekeeping 2026-08-29

## 2026-08-29
- chore: housekeeping 2026-08-29

## 2026-08-30
- chore: housekeeping 2026-08-30

## 2026-08-30
- chore: housekeeping 2026-08-30

## 2026-08-30
- chore: housekeeping 2026-08-30

## 2026-08-31
- chore: housekeeping 2026-08-31

## 2026-08-31
- chore: housekeeping 2026-08-31

## 2026-08-31
- chore: housekeeping 2026-08-31

## 2026-09-01
- chore: housekeeping 2026-09-01

## 2026-09-01
- chore: housekeeping 2026-09-01

## 2026-09-02
- chore: housekeeping 2026-09-02

## 2026-09-02
- chore: housekeeping 2026-09-02

## 2026-09-03
- chore: housekeeping 2026-09-03

## 2026-09-03
- chore: housekeeping 2026-09-03

## 2026-09-04
- chore: housekeeping 2026-09-04

## 2026-09-04
- chore: housekeeping 2026-09-04

## 2026-09-05
- chore: housekeeping 2026-09-05

## 2026-09-06
- chore: housekeeping 2026-09-06

## 2026-09-06
- chore: housekeeping 2026-09-06

## 2026-09-07
- chore: housekeeping 2026-09-07

## 2026-09-07
- chore: housekeeping 2026-09-07

## 2026-09-07
- chore: housekeeping 2026-09-07

## 2026-09-08
- chore: housekeeping 2026-09-08

## 2026-09-08
- chore: housekeeping 2026-09-08

## 2026-09-09
- chore: housekeeping 2026-09-09

## 2026-09-09
- chore: housekeeping 2026-09-09

## 2026-09-09
- chore: housekeeping 2026-09-09

## 2026-09-10
- chore: housekeeping 2026-09-10

## 2026-09-10
- chore: housekeeping 2026-09-10

## 2026-09-11
- chore: housekeeping 2026-09-11

## 2026-09-11
- chore: housekeeping 2026-09-11

## 2026-09-12
- chore: housekeeping 2026-09-12

## 2026-09-12
- chore: housekeeping 2026-09-12

## 2026-09-12
- chore: housekeeping 2026-09-12

## 2026-09-13
- chore: housekeeping 2026-09-13

## 2026-09-13
- chore: housekeeping 2026-09-13

## 2026-09-14
- chore: housekeeping 2026-09-14

## 2026-09-14
- chore: housekeeping 2026-09-14

## 2026-09-14
- chore: housekeeping 2026-09-14

## 2026-09-15
- chore: housekeeping 2026-09-15

## 2026-09-15
- chore: housekeeping 2026-09-15

## 2026-09-16
- chore: housekeeping 2026-09-16

## 2026-09-16
- chore: housekeeping 2026-09-16

## 2026-09-16
- chore: housekeeping 2026-09-16

## 2026-09-17
- chore: housekeeping 2026-09-17

## 2026-09-17
- chore: housekeeping 2026-09-17

## 2026-09-17
- chore: housekeeping 2026-09-17

## 2026-09-18
- chore: housekeeping 2026-09-18

## 2026-09-19
- chore: housekeeping 2026-09-19

## 2026-09-19
- chore: housekeeping 2026-09-19

## 2026-09-19
- chore: housekeeping 2026-09-19

## 2026-09-20
- chore: housekeeping 2026-09-20

## 2026-09-20
- chore: housekeeping 2026-09-20

## 2026-09-21
- chore: housekeeping 2026-09-21

## 2026-09-21
- chore: housekeeping 2026-09-21

## 2026-09-21
- chore: housekeeping 2026-09-21

## 2026-09-22
- chore: housekeeping 2026-09-22

## 2026-09-22
- chore: housekeeping 2026-09-22

## 2026-09-23
- chore: housekeeping 2026-09-23

## 2026-09-23
- chore: housekeeping 2026-09-23

## 2026-09-24
- chore: housekeeping 2026-09-24

## 2026-09-24
- chore: housekeeping 2026-09-24

## 2026-09-25
- chore: housekeeping 2026-09-25

## 2026-09-25
- chore: housekeeping 2026-09-25

## 2026-09-25
- chore: housekeeping 2026-09-25

## 2026-09-26
- chore: housekeeping 2026-09-26

## 2026-09-26
- chore: housekeeping 2026-09-26

