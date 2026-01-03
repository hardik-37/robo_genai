Controlled LLM Module
Overview

This project implements a controlled and reliable LLM module designed to embed a language model safely inside a software system.
The focus is on structure, validation, failure handling, and debuggability, not on prompt cleverness or model performance.

Prompt Management

All prompt instructions are defined in llm/prompts.py.

System instructions and user input are clearly separated.

Prompt wording can be changed without modifying core execution logic.

This is demonstrated in the prompt_change.py experiment.

Output Contracts

The model is instructed to return output in a strict JSON format.

An expected output structure is enforced (answer, confidence).

All model outputs are parsed and validated before use.

Invalid or malformed outputs are explicitly rejected and never silently accepted.

Failure Handling

If the model produces invalid output, the system retries a fixed number of times.

Each retry attempt is logged.

If retries are exhausted, the system fails gracefully with a clear error.

Silent failures are explicitly avoided.

Logging & Traceability

The system logs:

Prompt construction

Raw model responses

Validation failures

Retry attempts

This enables debugging and inspection after execution, even when failures occur.

Non-Determinism Awareness

Large Language Models are inherently non-deterministic and may produce different outputs for the same input.

This module acknowledges that behavior and enforces validation and retries to handle variability safely.

The current implementation uses a mocked LLM client to deterministically simulate failures for testing purposes.

Experiments

The experiments/ folder demonstrates:

A successful structured response

An invalid/malformed response

Retry and failure handling

Prompt changes without modifying core logic

Limitation

The current implementation uses a mocked LLM client and does not yet integrate a real LLM API.

Determinism controls and advanced output correction strategies are not implemented in this version.

Conclusion

This module provides a stable foundation for future systems such as retrieval-augmented generation (RAG), memory, and agentic workflows by enforcing explicit input/output boundaries and failure-aware behavior.