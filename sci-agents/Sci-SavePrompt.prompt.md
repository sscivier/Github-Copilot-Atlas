---
name: sci-savePrompt
description: Generalize a scientific analysis session into a reusable prompt file
tools: ['edit', 'search']
argument-hint: Optionally specify a title or focus area for the prompt (e.g. "GP uncertainty plot", "XArray preprocessing")
---

Generalize the current scientific analysis or workflow discussion into a reusable prompt that can be applied to similar scientific computing scenarios.

Think step by step:

1. Review the conversation to identify the user's primary scientific goal or workflow pattern
2. If no active conversation is present, tell the user this prompt expects an existing discussion to generalize
3. Identify the scientific domain context (e.g. GP regression, XArray processing, uncertainty visualization, PDE inversion)
4. Generalize into a reusable prompt for similar scientific scenarios — strip project-specific details (file names, variable names, dataset paths, model names) and replace with descriptive `<placeholder>` tokens
5. Extract the core scientific intent: method choices, numerical constraints, reproducibility requirements, output format expectations
6. Craft a generalized multi-line markdown prompt body with `<placeholder>` tokens for all variable elements
7. Create a concise camelCase title (1–3 words) for the slash command
8. Write a brief description (1 sentence, max 15 words)
9. Define an `argument-hint` describing what the user should provide at invocation time
10. Save the result to `untitled:${promptFileName}.prompt.md`

Output format:

```
---
name: ${camelCase title}
description: ${brief description}
argument-hint: ${expected inputs at invocation}
---

${generalized scientific prompt text with <placeholders>}
```

Scientific placeholder conventions:
- `<dataset>` — XArray Dataset or array input
- `<model>` — GP model, neural network, or statistical model
- `<domain>` — scientific application domain
- `<output_path>` — figure or results output location
- `<method>` — numerical method or algorithm
- `<invariant>` — mathematical property to test (e.g. symmetry, positivity, sum-to-one)
