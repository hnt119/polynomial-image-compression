# Small reproducible outputs

These JSON files are exact finite computations, not asymptotic proofs. Regenerate
them from the repository root:

```bash
python3 -m experiments local-images --polynomial all --primes 2 3 5 7 --q 1 > examples/local-images-original.json
python3 -m experiments local-images --polynomial all --primes 5 7 --q 35 > examples/local-images-q35.json
python3 -m experiments carriers --polynomial mixed-cubic --carrier geometric --size 8 --base 3 > examples/mixed-cubic-geometric.json
```

| File | Purpose |
| --- | --- |
| [Original local images](local-images-original.json) | Compare the five polynomials on four prime fields |
| [Deformed local images](local-images-q35.json) | Inspect the effect of one fixed deformation at its two prime divisors |
| [Mixed cubic carrier](mixed-cubic-geometric.json) | Check the image and energy of a same-set geometric progression |
