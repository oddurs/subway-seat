// StyleX compiles at build time through Babel. Next 16 picks this file up
// automatically for both Turbopack and webpack; postcss.config.js reuses it.
const path = require("path");

const dev = process.env.NODE_ENV !== "production";

module.exports = {
  presets: ["next/babel"],
  plugins: [
    [
      "@stylexjs/babel-plugin",
      {
        dev,
        runtimeInjection: false,
        enableInlinedConditionalMerge: true,
        treeshakeCompensation: true,
        aliases: {
          "@/*": [path.join(__dirname, "src", "*")],
        },
        unstable_moduleResolution: {
          type: "commonJS",
        },
      },
    ],
  ],
};
