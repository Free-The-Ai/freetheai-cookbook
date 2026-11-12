// The official freetheai JavaScript SDK: one reply, then a streamed reply.
//
//   npm install
//   FREETHEAI_API_KEY=ftai_... node example.mjs

import { FreeTheAI } from "freetheai";

const client = new FreeTheAI(); // reads FREETHEAI_API_KEY

const reply = await client.chat.completions.create({
  model: "glm-5.3",
  messages: [{ role: "user", content: "Write a haiku about open models." }],
});
console.log(reply.choices[0]?.message.content);

console.log("\nStreamed:");
for await (const text of client.chat.completions.streamText({
  model: "glm-5.3-flash",
  messages: [{ role: "user", content: "Count from one to five, one word per line." }],
})) {
  process.stdout.write(text);
}
console.log();
