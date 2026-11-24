# LifeBudget AI simulation

The local `lifebudget-ai` mock is a hand-authored OpenAI-compatible stand-in for `https://factory.marshub.uz/v1`. Its one example represents the expected `/chat/completions` response shape; it was not pulled from the provider and does not establish their contract or recommendation quality. No owner mock was searched because the provider workspace is not connected.

On 2026-11-24, the real Django audit endpoint ran against the simulation at `http://127.0.0.1:4010/ai`, with a disposable local user, a 7,000 UZS expense and a 12,000,000 UZS goal with 2,000,000 saved and 1,000,000 per month. The endpoint returned HTTP 200, 7,000 expenses, 10 months and a mock response. The simulation log recorded `POST /chat/completions` with status 200. This establishes local HTTP wiring and server arithmetic for this case, not provider behavior. Django tests separately exercise unavailable configuration and timeout by mocking the HTTP client. A real provider request awaits the user's API key.

Run with `postman simulation run postman/simulations/lifebudget-ai.sim.yaml --port 4010 --no-history`, setting `AI_BASE_URL=http://127.0.0.1:4010/ai`, `AI_API_KEY=local-simulation` and `AI_MODEL=simulation` on a local Django process. The stand-in does not model authentication or provider errors.
