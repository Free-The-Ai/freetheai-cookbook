# Vercel AI SDK

`createOpenAICompatible` from `@ai-sdk/openai-compatible` builds a provider for any OpenAI-compatible API. Pass the FreeTheAI base URL and key, then use the provider like any other model.

```bash
cd vercel-ai-sdk
npm install
FREETHEAI_API_KEY="ftai_..." npm start
```

The example shows `generateText` and `streamText`. The same provider works with `useChat` and other AI SDK helpers in a Next.js app.
