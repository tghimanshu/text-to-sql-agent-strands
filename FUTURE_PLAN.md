# Future Plan (Phase 2)

This document outlines the proposed enhancements and features for the next phase of the AWS Agent project.

## 1. Interactive Agent Interface
**Current State:** The agent runs a hardcoded message in `agent.py`.
**Phase 2 Goal:**
- Implement a command-line interface (CLI) to accept user input interactively.
- Allow users to choose different models or parameters via CLI arguments.

## 2. Enhanced Database Operations
**Current State:** `combine_sqlite_databases` is functional but basic.
**Phase 2 Goal:**
- Add conflict resolution strategies (e.g., skip, overwrite, merge).
- Support for other database types (e.g., PostgreSQL, MySQL).
- Add transaction rollback on failure to ensure atomicity across tables.

## 3. Robust Testing
**Current State:** No automated tests exist.
**Phase 2 Goal:**
- Add unit tests for `letter_counter` and `combine_sqlite_databases` using `pytest`.
- Add integration tests for the Agent to mock API calls and verify tool usage.

## 4. Extended Toolset
**Current State:** Only `letter_counter` is available.
**Phase 2 Goal:**
- Add AWS-specific tools (using `boto3`) to manage resources (e.g., S3 bucket listing, EC2 status checks).
- Integrate more complex math or data processing tools.

## 5. Deployment & Configuration
**Current State:** Local execution with `.env`.
**Phase 2 Goal:**
- Dockerize the application for consistent environments.
- Add configuration files (YAML/JSON) for managing agent prompts and tool settings.
