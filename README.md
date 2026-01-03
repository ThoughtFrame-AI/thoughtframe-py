# ThoughtFrame Python Runtime

This repository provides the **reference Python runtime for ThoughtFrame**.

It defines the execution model, routing semantics, and transport adapters
used to integrate Python modules into a ThoughtFrame system.

This package is **not an application** and does not run on its own.
It is intended to be embedded, configured, and launched by a host system.

---

## Purpose

ThoughtFrame supports multiple execution environments.
This project defines the **canonical Python-side runtime** so that Python
code can participate in a ThoughtFrame mesh in a predictable, disciplined way.

It exists to make it easy to build Python modules that:

- expose commands to ThoughtFrame
- receive structured requests
- return structured responses
- run synchronously or asynchronously
- communicate over standard transports

---

## What This Provides

- A strict command routing protocol (`module.method`)
- Deterministic module resolution and dispatch
- A minimal dependency-injected runtime catalog
- Reference transport implementations:
  - WebSocket-based command loop
  - HTTP dispatch endpoint
- A Python module contract (`BaseFrameModule`)

All transports delegate to the same routing and execution semantics.

---

## What This Does Not Provide

- No application logic
- No domain-specific behavior
- No task scheduling
- No plugin discovery system
- No automatic startup or background processes

All lifecycle control is explicit and owned by the host system.

---

## Core Concepts

### ModuleManager
A deterministic service registry used to construct and resolve runtime components.

### SystemCatalog
A stable access surface for runtime services such as routing, transport,
and configuration utilities.

### BaseFrameRouter
Enforces protocol correctness at runtime:
- `module.method` addressing
- exactly one request argument
- synchronous or asynchronous handlers
- strict resolution and validation

### FrameConnection
A reference WebSocket transport implementing handshake, keepalive,
and dispatch semantics.

### BaseWebServer
A reference HTTP transport that delegates all execution to the router.

### BaseFrameModule
The abstract base class for Python ThoughtFrame modules.

---

## Execution Model

- Nothing executes on import
- All wiring happens during explicit configuration
- All runtime behavior is opt-in
- The host system controls startup, shutdown, and lifecycle

This makes the runtime safe to embed and easy to reason about.

---

## Intended Usage

This package is designed to be depended on by:

- Python modules that expose functionality to ThoughtFrame
- Host systems that embed Python as an execution node
- Integration layers that need a stable Python runtime surface

Higher-level functionality belongs in separate packages.

---

## Stability and Versioning

Public interfaces and protocol semantics are treated as API.

Breaking changes will require a major version bump.
Non-breaking additions will be versioned conservatively.

---

## License

This project is licensed under the Apache License, Version 2.0.
See the LICENSE file for details.
