#!/usr/bin/env node

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const evalsDirectory = dirname(fileURLToPath(import.meta.url));
const sourcePath = join(evalsDirectory, "evals.json");
const outputPath = join(evalsDirectory, "cases.md");
const specification = JSON.parse(readFileSync(sourcePath, "utf8"));

function requireString(value, label) {
  if (typeof value !== "string" || value.trim() === "") {
    throw new Error(`${label} must be a non-empty string`);
  }
}

requireString(specification.skill_name, "skill_name");
requireString(specification.pass_condition, "pass_condition");
if (!Array.isArray(specification.evals) || specification.evals.length === 0) {
  throw new Error("evals must be a non-empty array");
}

const identifiers = new Set();
for (const [index, evaluation] of specification.evals.entries()) {
  if (!Number.isInteger(evaluation.id) || evaluation.id <= 0) {
    throw new Error(`evals[${index}].id must be a positive integer`);
  }
  if (identifiers.has(evaluation.id)) {
    throw new Error(`duplicate eval id ${evaluation.id}`);
  }
  identifiers.add(evaluation.id);
  requireString(evaluation.name, `evals[${index}].name`);
  requireString(evaluation.prompt, `evals[${index}].prompt`);
  requireString(evaluation.expected_output, `evals[${index}].expected_output`);
  if (!Array.isArray(evaluation.assertions) || evaluation.assertions.length === 0) {
    throw new Error(`evals[${index}].assertions must be a non-empty array`);
  }
  evaluation.assertions.forEach((assertion, assertionIndex) =>
    requireString(assertion, `evals[${index}].assertions[${assertionIndex}]`),
  );
}

const sortedIdentifiers = [...identifiers].sort((left, right) => left - right);
if (sortedIdentifiers.some((identifier, index) => identifier !== index + 1)) {
  throw new Error("eval ids must be contiguous and start at 1");
}

const quote = (value) => value.split("\n").map((line) => `> ${line}`).join("\n");
const lines = [
  "# Behavioral evaluation cases",
  "",
  "`evals.json` is authoritative. Regenerate this file with",
  "`node evals/render-cases.mjs --write`; verify parity with `--check`.",
  "",
  "Run each case in a fresh agent context with only `src/SKILL.md`, the case",
  "prompt, and any resource the skill itself instructs the agent to read. Do not",
  "give the agent the expected output or assertions. For every run, preserve the",
  "raw response, case ID, model and runtime identity (or `Unknown` when the host",
  "does not expose them), SHA-256 identity of the tested `src/` tree, resource",
  "availability, assertion-level grades, and any state the run changed.",
  "",
];

for (const evaluation of specification.evals) {
  lines.push(
    `## ${evaluation.id}. ${evaluation.name}`,
    "",
    "### Prompt",
    "",
    quote(evaluation.prompt),
    "",
    "### Expected output",
    "",
    evaluation.expected_output,
    "",
    "### Assertions",
    "",
    ...evaluation.assertions.map((assertion) => `- ${assertion}`),
    "",
  );
}

lines.push("## Pass condition", "", specification.pass_condition);
const rendered = `${lines.join("\n")}\n`;
const mode = process.argv[2];

if (mode === "--write") {
  writeFileSync(outputPath, rendered);
} else if (mode === "--check") {
  if (readFileSync(outputPath, "utf8") !== rendered) {
    throw new Error("cases.md is out of date; run with --write");
  }
} else {
  process.stdout.write(rendered);
}
