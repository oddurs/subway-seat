import stylex from "@stylexjs/eslint-plugin";
import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  {
    plugins: { "@stylexjs": stylex },
    rules: {
      "@stylexjs/valid-styles": "error",
      "@stylexjs/no-unused": "error",
      "@stylexjs/no-legacy-contextual-styles": "error",
      "@stylexjs/valid-shorthands": "warn",
      "@stylexjs/sort-keys": ["warn", { order: "recess" }],
    },
  },
  {
    // Babel and PostCSS load these as CommonJS.
    files: ["babel.config.js", "postcss.config.js"],
    rules: { "@typescript-eslint/no-require-imports": "off" },
  },
  globalIgnores([".next/**", "out/**", "build/**", "next-env.d.ts"]),
]);

export default eslintConfig;
