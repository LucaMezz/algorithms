export default {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "scope-enum": [
      2,
      "always",
      [
        "repo",
        "package",
        "docs",
        "ci",
        "deps",
        "tests",
        "examples",
        "benchmarks",

        "adts",
        "data-structures",
        "tracing",

        "searching",
        "sorting",
        "selection",
        "graphs",
        "greedy",
        "dynamic-programming",
        "shortest-paths",
        "flows",
        "strings",
        "compression",

        "arrays",
        "linked-lists",
        "stacks",
        "queues",
        "heaps",
        "hash-tables",
        "trees",
        "union-find",
      ],
    ],
  },
};