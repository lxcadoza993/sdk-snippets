/**
 * Create an item via the LynxFlow demo API.
 *
 * Uses the built-in fetch (Node 18+ or any modern browser).
 * No npm install needed.
 *
 * Usage:
 *   node create.js
 *   API_BASE=https://api.example.com node create.js
 */

const API_BASE = process.env.API_BASE || "https://demo-api.lynxflow.dev";
const ENDPOINT = `${API_BASE}/v1/items`;

const payload = { name: "hello", tags: ["demo"] };

console.log(`POST ${ENDPOINT}`);
console.log(`  body: ${JSON.stringify(payload)}`);

try {
  const resp = await fetch(ENDPOINT, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const body = await resp.json();
  console.log(`\nResponse (${resp.status}):`);
  console.log(JSON.stringify(body, null, 2));
} catch (err) {
  console.error(`\nError: ${err.message}`);
  process.exit(1);
}
