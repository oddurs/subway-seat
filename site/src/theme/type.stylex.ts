import * as stylex from "@stylexjs/stylex";

// Helvetica is the NYC subway's own face (the 1970 Vignelli/Noorda manual);
// Fraunces with its SOFT axis turned up is the living-room half: chunky and
// friendly, like 70s Cooper and Windsor. Fraunces and JetBrains Mono are loaded by
// next/font in layout.tsx; Helvetica comes from the system, with Arial as the fallback.
export const font = stylex.defineVars({
  sans: '"Helvetica Neue", Helvetica, Arial, sans-serif',
  display: 'var(--font-fraunces), "Cooper Black", Georgia, serif',
  mono: 'var(--font-jetbrains-mono), "JetBrains Mono", ui-monospace, Menlo, monospace',
});
