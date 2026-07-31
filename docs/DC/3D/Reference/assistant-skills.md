---
title: Tessa skills
diataxis: reference
tags: [reference, tessa, skills]
---

# Tessa skills

This page documents Tessa's six specialized skill domains, the kinds of agents in each, and how Tessa routes between them.

> *Available since IAPM v1.12 and Studio v0.7. Web integration not yet shipped.*

Skills are specialized domains that extend Tessa beyond diagnostics. Each skill contains multiple specialized agents that Tessa routes to automatically based on your request.

## Available Skill Domains

| Skill | Agents | What It Does |
|-------|--------|-------------|
| **Problem-Solving** | 9 | Systematic problem decomposition: research, analysis, architecture decisions, validation, synthesis, reviews, investigations, and reporting |
| **Engineering Team** | 10 | Full engineering workflow: architecture, backend, frontend, infrastructure, DevSecOps, QA, security review, incident response |
| **Red Team** | 11 | Offensive security methodology: reconnaissance, vulnerability analysis, exploitation, privilege escalation, lateral movement, persistence, exfiltration, reporting |
| **Adversary** | 3 | Adversarial quality reviews: strategy selection, execution against deliverables, LLM-as-Judge scoring |
| **NASA SE** | 10 | Systems engineering processes per NPR 7123.1D: requirements, architecture, verification, risk, reviews, integration, configuration |
| **Prompt Engineering** | 3 | Structured prompt construction, quality validation, constraint generation |

The **Red Team** skill requires explicit authorization before it runs, because its methodology is security-sensitive. Tessa asks you to approve it before proceeding. The other skills run without a separate approval step.

## How Skills Work

You don't invoke skills by name. Describe what you need and Tessa routes to the right skill and agents automatically.

```
"Review this code for security issues"     → Engineering Team (security agent)
"Help me debug why orders are failing"     → Problem-Solving (investigator agent)
"Analyze the architecture of auth-service" → Engineering Team (architect agent)
"What are the risks in this design?"       → NASA SE (risk agent) or Problem-Solving (analyst)
```

Each agent receives a focused brief, works with its own tool permissions, and reports back to Tessa who synthesizes the results for you.

## Multi-Agent Workflows

For complex requests, Tessa can orchestrate multiple agents in sequence or parallel. For example, asking "Do a full security review of my API" might engage:

1. **Engineering architect** - assess the design
2. **Security reviewer** - manual code review
3. **DevSecOps agent** - automated scanning methodology
4. **Engineering reviewer** - final quality gate

Tessa coordinates the workflow and presents consolidated findings.

## Browsing Available Skills

Ask Tessa what she can do:

!!! example "Try asking"
    - "What skills do you have?"
    - "What agents are available?"
    - "Can you do a security review?"

## Skills and Plans

Every plan has access to every skill. Tessa's full skill catalog is uniform across all Grid tiers (Start, Visualize, Analyze, Fuse) and all Tessa quality tiers (Basic, Professional, Premium). No plan unlocks, gates, or restricts a skill.

What changes by plan is **how much** you can use Tessa (usage per window) and **how smart** she is on hard problems (which model runs each operation), not **which** skills you can reach. A lower tier runs the same skills on a lighter model; it never loses a skill.

Where a boundary does exist, it gates an integration surface, not a reasoning skill: the same analytical capabilities remain reachable in Chat Mode on every tier. Check your account page for the current boundaries that apply to your plan.

## Related

- **For concept and design:** see [Tessa - Your AI Assistant](../Overview/ai-assistant.md).
- **For the diagnostic catalog:** see [Tessa diagnostics](assistant-diagnostics.md).
- **For prompt patterns by skill domain:** see [Write better prompts for Tessa](../How-to/assistant-prompts.md).
