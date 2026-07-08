# Workflow Folder

GitHub looks for active workflow files in this folder:

```text
.github/workflows/
```

This repository has three active workflows here:

- `ci.yml`
- `agent-plan.yml`
- `agent-execute.yml`

Important:

The YAML files inside `phases/*/examples/` are lesson examples only.

They are not active workflows because they are not inside `.github/workflows/`.

This separation is deliberate.

It lets students study more advanced workflow patterns without accidentally turning them on in the repository.

Do not put workflow files in `.github/actions/`.

`.github/actions/` is normally for custom reusable actions.

This repository does not currently use custom actions.
