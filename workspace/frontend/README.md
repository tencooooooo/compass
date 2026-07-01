# Compass Workspace

React + TypeScript read-only workspace for Compass generated reports.

## Local Data

Sync generated Compass outputs into the Vite public directory:

```bash
npm run sync-data
```

The app reads from:

```text
public/compass-data/
```

This directory is generated and ignored by Git.

## Development

```bash
npm install
npm run sync-data
npm run dev
```

## Build

```bash
npm run build
```

Future versions can replace the static data sync with an API without changing the UI pages substantially.
