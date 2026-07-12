# Harmony address conversion

This Python script reads EVM addresses from a text file and converts them to
the Harmony blockchain address format. It uses Harmony's official
[pyhmy](https://github.com/harmony-one/pyhmy) library.

## Usage

1. Install the dependency:

   ```bash
   python -m pip install pyhmy
   ```

2. Add one EVM address (`0x...`) per line to `wallets.txt`.
3. Run the converter:

   ```bash
   python conversion.py
   ```

Converted Harmony addresses are printed to standard output with line numbers.

## Notes

- Run the command from the repository root because the script reads
  `wallets.txt` using a relative path.
- Conversion results are printed to the terminal; the input file is not
  modified.
