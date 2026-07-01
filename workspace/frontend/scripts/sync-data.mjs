import { copyFileSync, existsSync, mkdirSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, "../../..");
const publicRoot = path.resolve(__dirname, "../public/compass-data");

const copyEntries = [
  ["reports", "reports"],
  ["config", "config"],
  ["storage/notifications", "storage/notifications"],
  ["memory/learning", "memory/learning"],
];

function ensureDir(dir) {
  mkdirSync(dir, { recursive: true });
}

function copyRecursive(source, target) {
  if (!existsSync(source)) return;
  const info = statSync(source);
  if (info.isDirectory()) {
    ensureDir(target);
    for (const entry of readdirSync(source)) {
      copyRecursive(path.join(source, entry), path.join(target, entry));
    }
    return;
  }
  ensureDir(path.dirname(target));
  copyFileSync(source, target);
}

function readJson(relativePath, fallback) {
  const fullPath = path.join(repoRoot, relativePath);
  if (!existsSync(fullPath)) return fallback;
  try {
    return JSON.parse(readFileSync(fullPath, "utf-8"));
  } catch {
    return fallback;
  }
}

if (existsSync(publicRoot)) {
  rmSync(publicRoot, { recursive: true, force: true });
}
ensureDir(publicRoot);

for (const [from, to] of copyEntries) {
  copyRecursive(path.join(repoRoot, from), path.join(publicRoot, to));
}

const discovery = readJson("reports/discovery/discovery_candidates.json", {});
const validation = readJson("reports/validation/validation_history.json", []);
const proposalIndex = readJson("reports/proposals/proposal_index.json", []);
const metrics = readJson("reports/learning/learning_metrics.json", {});

const manifest = {
  generatedAt: new Date().toISOString(),
  project: "Compass",
  dataRoot: "/compass-data",
  counts: {
    discovery: Array.isArray(discovery.candidates) ? discovery.candidates.length : 0,
    validation: Array.isArray(validation) ? validation.length : 0,
    proposals: Array.isArray(proposalIndex) ? proposalIndex.length : 0,
    learningApplied: Number(metrics.applied || 0),
  },
};

writeFileSync(path.join(publicRoot, "manifest.json"), JSON.stringify(manifest, null, 2), "utf-8");
console.log(`Compass data synced to ${publicRoot}`);
