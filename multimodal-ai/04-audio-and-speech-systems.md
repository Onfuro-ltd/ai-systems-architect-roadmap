# 04 — Audio and Speech Systems

## Purpose

Speech systems combine recognition, language reasoning, synthesis and real-time interaction. Timing, speaker identity, consent and acoustic uncertainty matter as much as transcript quality.

## Learning outcomes

By the end of this module, you should be able to:
- separate ASR, speaker/diarisation, reasoning and TTS responsibilities
- reason about streaming latency, turn-taking and interruption
- preserve timestamps and confidence for consequential evidence
- design consent, identity and retention controls for voice systems

## Speech recognition

ASR converts audio into text, often with timestamps. Accuracy varies with noise, accent, domain vocabulary, overlap and recording quality.

## Diarisation and speaker identity

Diarisation groups speech by speaker but does not automatically prove real-world identity. Identity-sensitive workflows require independent verification.

## Streaming

Real-time systems balance chunking, partial transcripts, endpoint detection and latency. Partial hypotheses can change as more audio arrives.

## Turn taking

Voice agents need interruption/barge-in, silence handling, cancellation and recovery. Conversation state should not rely only on generated text.

## Speech synthesis

TTS turns text into audio. Product design must account for voice selection, consent, accessibility, latency and misrepresentation risk.

## Evidence

Keep source audio or policy-approved references to segments when exact wording or speaker attribution affects a decision.

## Failure modes

- incorrect transcript changes meaning
- wrong speaker attribution
- agent speaks over or fails to stop for the user
- partial transcript triggers premature action
- synthetic voice mistaken for authenticated identity

## Security and governance

Voice can contain private information and biometric-like characteristics. Define consent, retention and access. Do not use voice synthesis or diarisation as proof of identity without an appropriate authentication mechanism.

## Evaluation

Measure word/error metrics where appropriate, but also task completion, semantic error severity, latency, interruption handling and human correction. Evaluate on representative accents/noise and domain terms.

## Practical exercise

Design a real-time support voice workflow. Include ASR, timestamps, interruption, retrieval/tools, approval for external action, TTS and a fallback to text/human support.

## Architect checklist

- [ ] audio and transcript provenance are linked
- [ ] speaker labels are not treated as identity proof
- [ ] partial transcripts cannot trigger unsafe actions
- [ ] latency budgets include recognition, reasoning and synthesis
- [ ] retention and consent are defined

## Primary reading

- [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356)
- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)

## Mastery gate

Design a production use of **Audio and Speech Systems** that preserves provenance, uncertainty and action boundaries, and state how you would measure whether the multimodal component improves the outcome over a simpler baseline.

## Takeaway

> Speech is a time-sensitive evidence stream; transcripts are useful representations, not perfect ground truth.

Next: **05 — Video Intelligence and Generation**.
