# Repository Guidelines

## Project Structure & Module Organization
- `pages/` holds the Next.js pages; `_app.tsx` wires Tailwind styles and `index.tsx` streams Markdown content from `/api`.
- `styles/` defines the Tailwind 4 theme and Markdown typography; extend tokens here before adding ad-hoc CSS.
- `api/` contains the FastAPI streaming service (`index.py`) and Pydantic settings loader (`config.py`) that read `OPENAI_API_KEY` from `.env`.
- Static assets belong in `public/`; core configs (`next.config.ts`, `tsconfig.json`, `postcss.config.mjs`, `eslint.config.mjs`) live at the repo root.

## Build, Test, and Development Commands
- `npm install` pulls frontend dependencies; run `pip install -r requirements.txt` (optionally inside `python -m venv .venv`) for the Python backend.
- `npm run dev` starts Next.js on `http://localhost:3000`; run `uvicorn api.index:app --reload --port 8000` alongside it and proxy `/api` to `http://localhost:8000/api` locally.
- `npm run build` compiles the production bundle; `npm run start` serves it; `npm run lint` executes the Next core-web-vitals ESLint profile.

## Coding Style & Naming Conventions
- TypeScript: author functional React components in PascalCase, state/hooks in camelCase, keep a 2-space indent, and prefer Tailwind utilities over inline styles.
- Python: follow PEP 8 with 4-space indents, snake_case functions, and keep streaming helpers isolated inside `api/index.py`.
- Run `npm run lint` before pushing and add targeted comments only when intent would otherwise be unclear.

## Testing Guidelines
- Automated tests are not yet configured; until they are, validate SSE rendering manually by exercising the UI against the streaming backend.
- When introducing tests, place frontend specs under `__tests__/` using React Testing Library or Vitest, and backend specs under `api/tests/` with pytest; mock OpenAI calls to avoid network/API drift.
- Document any new quality gates (e.g., `npm run test`, `pytest`) in this guide when you add them.

## Commit & Pull Request Guidelines
- Write concise, present-tense commit subjects (`feature: improve SSE buffering`) and add context in the body if necessary.
- PRs should summarize the change, note manual/automated verification, link tracking issues, and include screenshots or response samples for UI/API updates.
- Keep changes scoped, and update `AGENTS.md` or `README.md` when workflows or commands shift.

## Environment & Security Notes
- Store secrets in a local `.env` excluded from version control; set `OPENAI_API_KEY=...` so `api/config.py` can load it automatically.
- Avoid logging sensitive values and rotate keys immediately if exposed; align deployment configuration with the same variable names.
