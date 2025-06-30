import { generateApi } from "swagger-typescript-api";
import path from "path";

generateApi({
  output: path.resolve("./api"),
  input: path.resolve("./swagger.json"),
  modular: true,
  extractEnums: true,
  generateUnionEnums: false,
}).then(() => {
  console.log("✅ API client generated!");
});
