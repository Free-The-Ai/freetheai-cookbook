// The OpenAI Node SDK, pointed at FreeTheAI.
//
//   npm install
//   FREETHEAI_API_KEY=ftai_... node example.mjs

import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.freetheai.org/v1",
  apiKey: process.env.FREETHEAI_API_KEY,
});

const reply = await client.chat.completions.create({
  model: "glm-5.3",
  messages: [{ role: "user", content: "Name three uses for a paperclip." }],
  max_tokens: 200,
});
console.log(reply.choices[0].message.content);
