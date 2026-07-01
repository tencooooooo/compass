# Snapshot Rules

Snapshot rules protect Compass from future data leakage.

## Date Rule

For a snapshot date `D`, only records with dates `<= D` may be loaded.

## Data Rules

- Price rows after `D` are excluded.
- News after `D` is excluded.
- Events after `D` are excluded.
- Financial periods ending after `D` are excluded.
- Memory history after `D` is excluded.
- Knowledge versions created after `D` are excluded.

## Undated Data

Undated static company identity may be used only as reference metadata. Time-sensitive company metrics without dates must not be used for historical scoring.

Undated Knowledge markdown is only included when an active Knowledge version exists for the snapshot date.
