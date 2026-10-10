// The Vercel AI SDK with FreeTheAI, through createOpenAICompatible.
//
//   npm install
//   FREETHEAI_API_KEY=ftai_... node index.mjs

import { generateText, streamText } from "ai";
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";

const freetheai = createOpenAICompatible({
  name: "freetheai",
  baseURL: "https://api.freetheai.org/v1",
  apiKey: process.env.FREETHEAI_API_KEY,
});

const { text } = await generateText({
  model: freetheai("fta/zai/glm-5.3"),
  prompt: "Write a one-line tagline for a free AI API.",
});
console.log(text);

const result = streamText({
  model: freetheai("fta/zai/glm-5.3-flash"),
  prompt: "List three uses of embeddings, one per line.",
});
for await (const piece of result.textStream) {
  process.stdout.write(piece);
}
console.log();
