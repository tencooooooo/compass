# Filing Types

Initial supported forms:

- 10-K: annual report
- 10-Q: quarterly report
- 8-K: current report for material events

Future forms:

- DEF 14A: proxy statement
- S-1: registration statement
- Form 4: insider ownership changes

Compass should treat filing type as structured metadata. New forms should be added by extending parser configuration and validation rules, not by changing analysis engines.
