// scripts/patch-nuxt-tsconfig.ts
import fs from "fs";
import path from "path";

const tsconfigPath = path.resolve(".nuxt/tsconfig.json");
if (!fs.existsSync(tsconfigPath)) {
  console.error(
    "❌ .nuxt/tsconfig.json not found. Make sure Nuxt has been built first."
  );
  process.exit(1);
}

const config = JSON.parse(fs.readFileSync(tsconfigPath, "utf-8"));

config.exclude = Array.from(new Set([...(config.exclude ?? []), "../api"]));

fs.writeFileSync(tsconfigPath, JSON.stringify(config, null, 2));
console.log("✅ Patched .nuxt/tsconfig.json to exclude /api");
